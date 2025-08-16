import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Set up headless options
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Create the WebDriver instance
driver = webdriver.Chrome(options=chrome_options)

driver.maximize_window()


driver.get("https://shop.qaautomationlabs.com/index.php")


email_text=driver.find_element(By.XPATH,"//strong[text()='Email:']")

print(email_text.text)

password_text=driver.find_element(By.XPATH,"//strong[text()='Password:']")

print(password_text.text)

elements=driver.find_elements(By.CLASS_NAME,"help-block")

for element in elements:
    print(element.text)

heading=driver.find_element(By.XPATH,"//span[text()='Login']")
headingtext=heading.text

assert password_text.is_displayed() is True,f"Assertion failed."
assert email_text.is_displayed() is True,f"Assertion failed."
assert heading.is_displayed() is True,f"Assertion failed."
assert headingtext=="Login",f"Assertion failed."

breadcrumb=driver.find_element(By.CLASS_NAME,"breadcrumb-item.active")

breadcrumb_text=breadcrumb.text

assert breadcrumb_text=="Login",f"Assertion Failed."
print(f"breadcrumb active text is:{breadcrumb_text}")
    
print("test passed..")
driver.close()