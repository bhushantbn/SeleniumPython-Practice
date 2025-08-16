import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

# Set up headless options
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Create the WebDriver instance
driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 10)
driver.maximize_window()
# Navigate to site and click on "Form" link
driver.get("https://formy-project.herokuapp.com/")
wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Form"))).click()

# Verify the heading
heading = wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1"))).text
assert "Form" in heading
print(heading)

# Fill out the form
wait.until(EC.visibility_of_element_located((By.ID, "first-name"))).send_keys("John")
driver.find_element(By.ID, "last-name").send_keys("Doe")
driver.find_element(By.ID, "job-title").send_keys("Software Engineer")

# Select radio button and checkbox
driver.find_element(By.XPATH, "//input[@value='radio-button-1']").click()
driver.find_element(By.XPATH, "//input[@value='checkbox-1']").click()

# Select from dropdown
dropdown = driver.find_element(By.ID, "select-menu")
dropdown.click()
wait.until(EC.element_to_be_clickable((By.XPATH, "//option[@value='2']"))).click()

# Pick a date
date_input = driver.find_element(By.ID, "datepicker")
date_input.click()
driver.execute_script("window.scrollTo(0, 500);")
# Wait and click a specific date (adjust timestamp as needed)
wait.until(EC.element_to_be_clickable((By.XPATH, "//td[@data-date='1754265600000']"))).click()

print("Form filled successfully")

# Close browser
driver.close()
