# handleNewtab.py

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver=webdriver.Chrome()

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

driver.find_element(By.XPATH,"//a[text()='Events']").click()

time.sleep(2)
tabs=driver.window_handles

driver.switch_to.window(tabs[1])

print("new tab url:",driver.current_url)
time.sleep(2)
driver.close()
driver.switch_to.window(tabs[0])
time.sleep(2)
assert driver.current_url=="https://shop.qaautomationlabs.com/shop.php",f"Assertion failed."
print("assert passed.")
print("Back to original tab:", driver.current_url)
driver.quit()
