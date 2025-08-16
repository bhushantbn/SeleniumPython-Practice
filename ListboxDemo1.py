# This script automates the interaction with a list box on a demo website.
# It selects multiple items from one list, moves them to another, and verifies the transfer.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://testing.qaautomationlabs.com/")
driver.execute_script("window.scrollBy(0,500);")

link = driver.find_element(By.LINK_TEXT, "List Box")
link.click()
assert "List Box Demo" in driver.title, "Assertion failed"

# Multi-select List1
list1 = driver.find_element(By.ID, "list1")
select = Select(list1)
select.select_by_index(2)
select.select_by_index(1)

# Print selected options in List1
selected_texts = [opt.text for opt in select.all_selected_options]
print("Selected in List1:", selected_texts)

# Click Add button
driver.find_element(By.ID, "add").click()
time.sleep(1)

# Verify in List2
list2 = driver.find_element(By.ID, "list2")
select_list2 = Select(list2)
options_in_list2 = [opt.text for opt in select_list2.options]
print("Options in List2:", options_in_list2)

# Assert all selected options moved
for i,text in enumerate(selected_texts,start=1):
    assert text in options_in_list2, f"Assertion failed: {text} not found in List2"
    print(i,". ",text)
print("All selected options successfully moved ✅")

time.sleep(2)
driver.quit()
