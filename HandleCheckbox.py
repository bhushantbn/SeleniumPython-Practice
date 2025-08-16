from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://formy-project.herokuapp.com")

link = driver.find_element(By.LINK_TEXT, "Checkbox")
link.click()
print("Checkbox page opened.")
time.sleep(1)   
checkbox = driver.find_element(By.ID, "checkbox-1")
checkbox.click()
value=checkbox.get_attribute("value")
print("Checkbox value:", value)

time.sleep(1)
driver.quit()
