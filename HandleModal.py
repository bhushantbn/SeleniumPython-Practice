import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()

driver.get("https://formy-project.herokuapp.com")

driver.execute_script("window.scrollBy(0,500);")

element=driver.find_element(By.LINK_TEXT,"Modal")
element.click()
time.sleep(2)
h1=driver.find_element(By.XPATH,"//h1[text()='Modal']")
assert h1.is_displayed()
print("assertion is passed.")
openModal=driver.find_element(By.ID,"modal-button")
openModal.click()
time.sleep(2)
modal=driver.find_element(By.CLASS_NAME,"modal-content")
assert modal.is_displayed() is True,"assertion failed.."
#print("2nd assretion is passed.")
time.sleep(2)
closeBtn=driver.find_element(By.ID,"close-button")

assert closeBtn.is_displayed() is True,"assertion failed.."
closeBtn.click()
time.sleep(2)
driver.close()
