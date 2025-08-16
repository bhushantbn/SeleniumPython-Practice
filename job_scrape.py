from playwright.sync_api import sync_playwright
import pandas as pd
import time

def scrape_glassdoor(url, pages=1):
    jobs = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=200)
        page = browser.new_page()

        # Go to the Glassdoor jobs page
        page.goto(url, timeout=60000)

        # Handle cookies/consent popup if present
        try:
            page.locator("button:has-text('Accept All')").click(timeout=5000)
        except:
            pass

        for page_no in range(1, pages+1):
            print(f"Scraping page {page_no}...")

            # Wait until job list is visible
            page.wait_for_selector("article", timeout=30000)

            jobs_on_page = page.locator("article")
            count = jobs_on_page.count()

            for i in range(count):
                try:
                    title = jobs_on_page.nth(i).locator("a.jobLink").inner_text()
                except:
                    title = ""
                try:
                    company = jobs_on_page.nth(i).locator("div.jobHeader a").inner_text()
                except:
                    company = ""
                try:
                    location = jobs_on_page.nth(i).locator("span.loc").inner_text()
                except:
                    location = ""
                try:
                    posted = jobs_on_page.nth(i).locator("div.jobLabels span").inner_text()
                except:
                    posted = ""

                jobs.append({
                    "Title": title.strip(),
                    "Company": company.strip(),
                    "Location": location.strip(),
                    "Posted": posted.strip()
                })

            # Go to next page if available
            try:
                next_button = page.locator("a[data-test='pagination-next']")
                if next_button.is_visible():
                    next_button.click()
                    time.sleep(3)
                else:
                    break
            except:
                break

        browser.close()

    return pd.DataFrame(jobs)


if __name__ == "__main__":
    url = "https://www.glassdoor.co.in/Job/ahmedabad-senior-qa-analyst-jobs-SRCH_IL.0,9_IC2935226_KO10,27.htm?sortBy=date_desc"
    df = scrape_glassdoor(url, pages=2)
    print(df)
    df.to_csv("glassdoor_jobs.csv", index=False)
