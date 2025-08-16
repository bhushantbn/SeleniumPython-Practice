import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()

driver.get("https://formy-project.herokuapp.com/")

link=driver.find_element(By.LINK_TEXT,"Datepicker")

link.click()
time.sleep(2)

date_input=driver.find_element(By.ID,"datepicker")
assert date_input.is_displayed(),"Assertion failed.."

datepicker=driver.execute_script("arguments[0].value='2025-08-15';",date_input)
print("Assertion passed..")
time.sleep(2)

driver.quit()