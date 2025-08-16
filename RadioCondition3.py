import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://testing.qaautomationlabs.com/radio-button.php")

# Locate the label containing 'Male' and then find the input inside it
maleRadioLabel = driver.find_element(By.XPATH, "//div[@class='col-6']//label[contains(text(),'Male')]")
maleRadioInput = maleRadioLabel.find_element(By.XPATH, ".//input")

# Click the radio button
maleRadioInput.click()
print("Label text:", maleRadioLabel.text)

time.sleep(2)


driver.execute_script("window.scrollBy(0,500);")
time.sleep(3)

# Get the result text

age_group_label = driver.find_element(By.XPATH,"//input[@value='Under 18']")
age_group_label.click()

# Click 'Show Selected Values' button
show_button = driver.find_element(By.XPATH, "//button[text()='Show Selected Values']")
show_button.click()


time.sleep(2)

    
# Assertions
assert maleRadioInput.is_selected(), "Assertion failed: Male radio button is not selected"

assert age_group_label.is_selected(), "Assertion failed: Age group label is not selected"

result_text = driver.find_element(By.ID, "result3")
print("Result text:", result_text.text)

assert result_text.text.strip() == "You selected: Gender = Male, Age Group =Under 18", "Assertion failed: Result text does not match"

print("All assertions passed ✅")

time.sleep(2)
driver.quit()
