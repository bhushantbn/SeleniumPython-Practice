#verifyCategoryPageGuestUser.py

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver=webdriver.Chrome()

driver.maximize_window()

driver.get("https://shop.qaautomationlabs.com/index.php")

hoverElement=driver.find_element(By.XPATH,"//a[text()='Shop ']")

time.sleep(2)
actions=ActionChains(driver)
actions.move_to_element(hoverElement).perform()

hoveredElement=driver.find_element(By.XPATH,"//a[text()='Womens Wear']")
hoveredElement.click()


assert driver.title=="This Page Does Not Exist",f"assertion failed"

print("pass")
time.sleep(2)
driver.quit()