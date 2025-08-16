#RadioCondition1.py

# This script uses Selenium to test radio buttons on a webpage.
# It verifies the total number of radio buttons and the number of disabled radio buttons.



import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()

driver.get("https://testing.qaautomationlabs.com/radio-button.php")

radioButton=driver.find_element(By.LINK_TEXT,"Radio Button")
radioButton.click()

radioCount=driver.find_elements(By.XPATH, "//input[@type='radio']")

disabled_count=sum(1 for rb in radioCount if not rb.is_enabled())
assert disabled_count == 1,f"assertion failed."
print(disabled_count)

assert len(radioCount) == 10,f"assertion failed."

print("passed...")


time.sleep(2)
driver.quit()
