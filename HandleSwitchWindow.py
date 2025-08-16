import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()

driver.get("https://formy-project.herokuapp.com/")
driver.execute_script("window.scrollBy(0,500);")
time.sleep(2)

link=driver.find_element(By.LINK_TEXT,"Switch Window")
link.click()
time.sleep(2)
openlink=driver.find_element(By.ID,"new-tab-button")
openlink.click()
time.sleep(2)
driver.close()