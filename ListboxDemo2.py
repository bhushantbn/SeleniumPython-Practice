# This script automates testing of a list box functionality on a demo website.
# It selects items from a source list, moves them to a destination list, 
# and then verifies that the correct number of items were moved and remain in the source list.

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


driver=webdriver.Chrome()
driver.maximize_window()

driver.get("https://testing.qaautomationlabs.com/")

driver.execute_script("window.scrollBy(0,500);")

link=driver.find_element(By.LINK_TEXT,"List Box")
link.click()

list1=driver.find_element(By.ID,"list1")
select=Select(list1)
select.select_by_index(2)
select.select_by_index(1)

for opt in select.all_selected_options:
    print("Removed options from List 1:",opt.text)

driver.find_element(By.ID,"add").click()
time.sleep(2)

list2=driver.find_element(By.ID,"list2")
select_list2=Select(list2)

for opt in select_list2.options:
    print("Added options to List 2:",opt.text)

assert len(select_list2.options) == 2,f"Assertion failed.."
print("1st Assertion passed..")

assert len(select.options)==8,f"Assertion failed.."
print("2nd Assertion passed..")


time.sleep(2)
driver.quit()