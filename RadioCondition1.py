#RadioCondition1.py

# This script uses Selenium to test radio buttons on a webpage.
# It verifies the total number of radio buttons and the number of disabled radio buttons.

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
# Set up headless options
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--window-size=1920,1080")


# Create the WebDriver instance
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()
wait = WebDriverWait(driver, 20)

driver.get("https://testing.qaautomationlabs.com/radio-button.php")

radioCount=driver.find_elements(By.XPATH, "//input[@type='radio']")

disabled_count=sum(1 for rb in radioCount if not rb.is_enabled())
assert disabled_count == 1,f"assertion failed."
print(disabled_count)

assert len(radioCount) == 10,f"assertion failed."

print("passed...")


time.sleep(2)
driver.quit()
