from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Headless setup
chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://shop.qaautomationlabs.com/index.php")

# Use JS to click submenu directly
submenu = driver.find_element(By.XPATH, "//a[text()='Womens Wear']")
driver.execute_script("arguments[0].scrollIntoView(true); arguments[0].click();", submenu)

time.sleep(2)  # optional: wait for page navigation
print("Clicked Womens Wear ✅")
print(driver.current_url)

driver.quit()
