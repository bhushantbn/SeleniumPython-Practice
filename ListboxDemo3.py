# This script tests the functionality of a dual list box.
# It automates moving all items from one list to another, verifying the transfer.
# It then selects and removes specific items from the second list, and verifies the final state.

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
select_list1 =Select(list1)


for option in select_list1.options:
    print("Removed options from List 1:",option.text)

selected_texts=[opt.text for opt in select_list1.all_selected_options]
#print(selected_texts)

for option in select_list1.options:
    select_list1.select_by_visible_text(option.text)

add_button=driver.find_element(By.ID,"add")
add_button.click()
time.sleep(2)
assert len(select_list1.options)==0,f"Assertion failed.."
print("1st Assertion passed..")

list2=driver.find_element(By.ID,"list2")
select_list2=Select(list2)

print("Options in List2:")
for opt in select_list2.options:
    print("Added options to List 2:",opt.text)

assert len(select_list2.options)==10,f"Assertion failed.."
print("2n2 Assertion passed..")

select_list2.deselect_all()
time.sleep(2)
select_list2.select_by_index(0)
select_list2.select_by_index(1)
select_list2.select_by_index(2)
removed_options = [opt.text for opt in select_list2.all_selected_options]

remove_button=driver.find_element(By.ID,"remove")
remove_button.click()
# Print removed options
print("Removed options from List2:")
for opt_text in removed_options:
    print(opt_text)
remaining_options = [opt.text for opt in select_list2.options]
print("Remaining options in List2:", remaining_options)


assert len(select_list2.options)==7,f"Assertion failed.."
print("3rd Assertion passed..")

time.sleep(2)
driver.quit()