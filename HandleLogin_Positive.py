from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()

driver.get("https://shop.qaautomationlabs.com/index.php")

driver.execute_script("window.scrollBy(0,500);")
time.sleep(2)

driver.find_element(By.ID,"email").send_keys("demo@demo.com")
driver.find_element(By.ID,"password").send_keys("demo")
driver.find_element(By.ID,"loginBtn").click()

expected_URL="https://shop.qaautomationlabs.com/shop.php"

assert driver.current_url == expected_URL,f"Assertion failed.."  

print("URL Assertion passed.")

driver.close()
