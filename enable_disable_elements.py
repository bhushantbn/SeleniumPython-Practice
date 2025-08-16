import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver=webdriver.Chrome()

driver.maximize_window()
driver.get("https://formy-project.herokuapp.com")
driver.execute_script("window.scrollBy(0, 500);")
time.sleep(2)
link=driver.find_element(By.LINK_TEXT,"Enabled and disabled elements")

value=link.text
print("value is:",value)

link.click()
time.sleep(2)

disable_element=driver.find_element(By.ID,"disabledInput")
enable_element=driver.find_element(By.ID,"input")

assert disable_element.is_enabled() is False,"Element is visible"
print("first Assertion passed.")

assert enable_element.is_enabled() is True, "Element is not visible"
print ("2nd Assertion passed.")

heading = driver.find_element(By.XPATH,"//h1[text()='Enabled and Disabled elements']")
assert heading.is_displayed()
print("3rd assertion passed.")

driver.close()