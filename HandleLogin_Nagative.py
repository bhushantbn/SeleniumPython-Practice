from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Firefox()
driver.maximize_window()

driver.get("https://shop.qaautomationlabs.com/index.php")

driver.execute_script("window.scrollBy(0,500);")

driver.find_element(By.ID, "email").send_keys("demo1@demo.com")
driver.find_element(By.ID, "password").send_keys("demo1")
driver.find_element(By.ID, "loginBtn").click()

# Wait until the error message appears
wait = WebDriverWait(driver, 10)
error_message = wait.until(EC.visibility_of_element_located((By.ID, "errorMsg")))

# Assert the message
assert error_message.text.strip() == "Invalid email or password!", \
    f"Expected 'Invalid email or password!' but got '{error_message.text}'"

#time.sleep(2);
print("Error message assertion passed.")

driver.quit()
