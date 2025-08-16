#RadioCondition2.py

# This script uses Selenium to find and interact with a specific radio button on a webpage.
# It locates the 'Male' radio button, extracts and prints its label text, and then clicks on it.

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

driver.get("https://testing.qaautomationlabs.com/radio-button.php")
maleRadioButton=driver.find_element(By.XPATH,"(//input[@value='Male'])")
label_text = maleRadioButton.find_element(By.XPATH, "./ancestor::label").text
print(f"text is: {label_text}")
maleRadioButton.click()

element=driver.find_element(By.XPATH,"//button[text()='Show Selected Gender']")
element.click()

maleRadioCondition=driver.find_element(By.ID,"result").text
assert maleRadioCondition == "You selected: Male",f"assertion failed."
print(f"{maleRadioCondition}")

time.sleep(3)

femaleRadioButton=driver.find_element(By.XPATH,"//input[@value='Female']")
label_text = femaleRadioButton.find_element(By.XPATH, "./ancestor::label").text
print(f"text is: {label_text}")
femaleRadioButton.click()
newelement=driver.find_element(By.XPATH,"//button[text()='Show Selected Gender']")
newelement.click()

femaleRaddioCondition=driver.find_element(By.ID,"result").text
assert femaleRaddioCondition == "You selected: Female",f"assertion failed."
print(f"{femaleRaddioCondition}")

time.sleep(2)
driver.quit()   