import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.maximize_window()

driver.get("https://shop.qaautomationlabs.com/index.php")

driver.find_element(By.ID,"email").send_keys("")
driver.find_element(By.ID,"password").send_keys("")
element=driver.find_element(By.ID,"loginBtn")
element.click()

time.sleep(2)
visibleElement=driver.find_element(By.ID,"emailerror")

assert visibleElement.is_displayed() is True,f"Assertion failed"

print("Passed.")


driver.close()
