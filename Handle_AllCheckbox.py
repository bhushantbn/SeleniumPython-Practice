import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://shop.qaautomationlabs.com/index.php")

# wait=webdriver.wait(driver,10)
link=driver.find_element(By.XPATH,'//a[text()="Testing"]')
link.click()

driver.switch_to.window(driver.window_handles[-1])

time.sleep(2)
driver.find_element(By.XPATH,"//p[normalize-space(text())='CheckBox']").click()
toggleBtn=driver.find_element(By.ID,"toggleBtn")
toggleBtn.click()

assert toggleBtn.text=="Uncheck All",f"Assertion failed"

print("Assertion passed")

checkboxes=driver.find_elements(By.XPATH,"//input[@type='checkbox']")
checked_boxes=  [cb for cb in checkboxes if cb.is_selected()]

assert len(checked_boxes) ==4,f"assertion failed.." 

print("checkboxes assertions passed..")

time.sleep(2)

driver.quit()