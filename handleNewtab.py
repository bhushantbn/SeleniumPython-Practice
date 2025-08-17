# handleNewtab_events.py

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Headless Chrome setup
chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--window-size=1920,1080")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)
wait = WebDriverWait(driver, 20)

# Navigate to site
driver.get("https://shop.qaautomationlabs.com/index.php")

# Login
driver.find_element(By.ID, "email").send_keys("demo@demo.com")
driver.find_element(By.ID, "password").send_keys("demo")
driver.find_element(By.ID, "loginBtn").click()

# Wait for main page to load
wait.until(EC.url_contains("/shop.php"))

# Locate 'Events' link and scroll into view
events_link = wait.until(EC.presence_of_element_located((By.XPATH, "//a[text()='Events']")))
driver.execute_script("arguments[0].scrollIntoView(true);", events_link)

# Click and switch to the new tab
events_link.click()
time.sleep(2)  # brief wait for tab to open
tabs = driver.window_handles
driver.switch_to.window(tabs[-1])

print("New tab URL:", driver.current_url)

# Close new tab and return to original
driver.close()
driver.switch_to.window(tabs[0])
print("Back to original tab URL:", driver.current_url)

driver.quit()
