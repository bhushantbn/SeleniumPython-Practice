# This script automates the testing of a dual list box feature, focusing on moving items back and forth.
# It first transfers all items from a source list to a destination list, verifying the move.
# It then selects a subset of items from the destination list and moves them back to the source list,
# verifying the final item counts in both lists.

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
select_list1=Select(list1)


selected_texts=[opt.text for opt in select_list1.all_selected_options]
#print(selected_texts)

for option in select_list1.options:
    select_list1.select_by_visible_text(option.text)
    print(f"Removed options from List 1:",option.text)


addButton=driver.find_element(By.ID,"add")
addButton.click()
time.sleep(2)

assert len(select_list1.options)==0,f"Assertion failed.."
print("1st Assertion passed.. List 1 cleared..")

list2=driver.find_element(By.ID,"list2")
select_list2=Select(list2)

for opt in select_list2.options:
    print("Added options to List 2:",opt.text)

assert len(select_list2.options)==10,f"Assertion failed.."
print("2nd Assertion passed.. all options added to List 2")

select_list2.deselect_all()
time.sleep(2)

removed_options=[opt.text for opt in select_list2.all_selected_options]
print("Removed options from List 2:",removed_options)

select_list2.select_by_index(0)
select_list2.select_by_index(1)
select_list2.select_by_index(2)

remaining_options=[opt.text for opt in select_list2.options]
print("Remaining options in List 2:",remaining_options)

removeButton=driver.find_element(By.ID,"remove")
removeButton.click()
time.sleep(2)

assert len(select_list2.options)==7,f"Assertion failed.."
print("3rd Assertion passed..")

remaining_options=[opt.text for opt in select_list2.options]
print("Remaining options in List 2:",remaining_options)

time.sleep(2)

updated_options=[opt.text for opt in select_list1.options]
print("updated options in List 1:",updated_options)


assert len(select_list1.options)==3,f"Assertion failed.."
print("4th Assertion passed..")

time.sleep(2)

driver.quit()