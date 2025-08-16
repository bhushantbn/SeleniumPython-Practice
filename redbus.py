from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime


def select_location(driver, wait, location_data):
    """Type location and select from suggestion list"""
    search_textbox = driver.switch_to.active_element
    search_textbox.send_keys(location_data)

    search_category_locator = (By.XPATH, "//div[contains(@class, 'searchCategory')]")
    search_list = wait.until(EC.presence_of_all_elements_located(search_category_locator))

    print("Search list count:", len(search_list))

    location_search_result = search_list[0]
    location_name_locator = ".//div[contains(@class, 'listHeader')]"
    location_list = location_search_result.find_elements(By.XPATH, location_name_locator)
    print("Location list count:", len(location_list))

    for location in location_list:
        l_name = location.text.strip()
        if l_name.lower() == location_data.lower():
            location.click()
            break


def main():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=chrome_options)
    wait = WebDriverWait(driver, 15)

    # Visit redbus.in
    driver.get("https://www.redbus.in")

    # Select source
    source_button_locator = (By.XPATH, "//div[contains(@class, 'srcDestWrapper') and @role='button']//div[text()='From']")
    source_button = wait.until(EC.visibility_of_element_located(source_button_locator))
    source_button.click()

    source_suggestion_locator = (By.XPATH, "//div[contains(@class, 'searchSuggestionWrapper')]")
    wait.until(EC.visibility_of_element_located(source_suggestion_locator))
    select_location(driver, wait, "Pune")

    # Select destination
    select_location(driver, wait, "Hyderabad")

    # --- Date Selection Fix ---
    # Open date picker by clicking the calendar wrapper (not hidden input)
    date_wrapper_locator = (By.XPATH, "//div[contains(@class,'labelCalendarContainer')]")
    wait.until(EC.element_to_be_clickable(date_wrapper_locator)).click()

    # Select tomorrow's date (fallback to day after tomorrow)
    tomorrow = (datetime.date.today() + datetime.timedelta(days=1)).day
    date_locator = (By.XPATH, f"//table[contains(@class,'rb-monthTable')]//span[text()='{tomorrow}']")

    try:
        wait.until(EC.element_to_be_clickable(date_locator)).click()
        print("Date selected:", tomorrow)
    except:
        day_after = (datetime.date.today() + datetime.timedelta(days=2)).day
        fallback_locator = (By.XPATH, f"//table[contains(@class,'rb-monthTable')]//span[text()='{day_after}']")
        wait.until(EC.element_to_be_clickable(fallback_locator)).click()
        print("Date selected:", day_after)

    # Click search
    search_button_locator = (By.XPATH, "//button[contains(@class, 'searchButtonWrapper')]")
    search_button = wait.until(EC.element_to_be_clickable(search_button_locator))
    search_button.click()

    # Wait for results container
    results_container_locator = (By.XPATH, "//div[contains(@class,'busFound')]")
    wait.until(EC.presence_of_element_located(results_container_locator))

    # Try clicking Primo if available
    primo_button_locator = (By.XPATH, "//div[contains(text(),'Primo')]")
    try:
        primo_button = wait.until(EC.element_to_be_clickable(primo_button_locator))
        primo_button.click()
        print("✅ Primo filter applied")
    except:
        print("⚠️ Primo filter not available for this route")

    # Subtitle check
    sub_title_locator = (By.XPATH, "//span[contains(@class, 'subtitle')]")
    wait.until(EC.text_to_be_present_in_element(sub_title_locator, "buses"))
    sub_title = wait.until(EC.visibility_of_element_located(sub_title_locator))
    print(sub_title.text)

    # Scroll until End of list
    tuple_wrapper_locator = (By.XPATH, "//li[contains(@class, 'tupleWrapper')]")
    buses_name_locator = ".//div[contains(@class, 'travelsName')]"

    while True:
        row_list = wait.until(EC.presence_of_all_elements_located(tuple_wrapper_locator))
        end_of_list = driver.find_elements(By.XPATH, "//span[contains(text(),'End of list')]")

        if end_of_list:
            break

        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth'});", row_list[-3])
        wait.until(lambda d: len(d.find_elements(*tuple_wrapper_locator)) > len(row_list))

    # Print buses list
    row_list = wait.until(EC.presence_of_all_elements_located(tuple_wrapper_locator))
    print("Total number of buses:", len(row_list))
    for row in row_list:
        print(row.find_element(By.XPATH, buses_name_locator).text)

    print("✅ Script finished successfully")
    driver.quit()


if __name__ == "__main__":
    main()
