import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()

driver.get("https://testing.qaautomationlabs.com/web-table.php")

driver.execute_script("window.scrollBy(0,500);")

assert "Table Demo" in driver.title,f"Assertion failed.."
print("1st Assertion passed..")
time.sleep(2)

searchbox=driver.find_element(By.ID,"searchInput")
searchbox.send_keys("India")

# need to add code


driver.quit()