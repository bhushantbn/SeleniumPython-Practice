import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver=webdriver.Chrome()

driver.maximize_window()

wait=WebDriverWait(driver,10)

driver.get("https://shop.qaautomationlabs.com/index.php")

print(driver.title)
print(driver.current_url)

driver.find_element(By.XPATH,"//a[text()='Testing']").click()


driver.switch_to.window(driver.window_handles[-1])

print(driver.title)
print(driver.current_url)

time.sleep(2)
driver.find_element(By.XPATH,"//p[normalize-space()='Radio Button']").click()
print(driver.current_url)

assert "Radio Button" in driver.title ,f"does not exist title"

print(f"test passed.,{driver.title}")


driver.quit()