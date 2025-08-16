#verifyCategoryPageLoginUser.py


import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

# Set up headless options
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Create the WebDriver instance
driver = webdriver.Chrome(options=chrome_options)

driver.maximize_window()

driver.get("https://shop.qaautomationlabs.com/index.php")

driver.find_element(By.ID,"email").send_keys("demo@demo.com")
driver.find_element(By.ID,"password").send_keys("demo")
loginButton=driver.find_element(By.ID,"loginBtn")

loginButton.click()
expectedURL="https://shop.qaautomationlabs.com/shop.php"

assert driver.current_url == expectedURL,f"assertion failed"

print("passed")

time.sleep(2)

actions=ActionChains(driver)

hoverElement=driver.find_element(By.XPATH,"//a[text()='Shop ']")

actions.move_to_element(hoverElement).perform()

hoveredElement=driver.find_element(By.XPATH,"//a[text()='View All']")

hoveredElement.click()
time.sleep(2)

breadcrumb=driver.find_element(By.XPATH,"//a[text()='Shop']")
# breadcrumb_text=breadcrumb.text
assert breadcrumb.text=="Shop",f"Assertion failed"

print(breadcrumb.text)
print("2nd assertion passed.")
time.sleep(2)
driver.quit()
