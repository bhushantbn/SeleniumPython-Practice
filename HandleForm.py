import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# Set up headless options
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Set up the service to manage the WebDriver executable
# This is the correct way to integrate webdriver-manager with Selenium 4+
service = Service(ChromeDriverManager().install())

# Create the WebDriver instance
# The 'service' and 'options' are now passed as keyword arguments
driver = webdriver.Chrome(service=service, options=chrome_options)
wait = WebDriverWait(driver, 20)  # Increased wait time to 20 seconds
driver.maximize_window()

# Navigate to site and click on "Form" link

driver.get("https://formy-project.herokuapp.com/")
print("Navigated to the home page.")
time.sleep(2)

# Wait for the "Form" link to be present and then click it
form_link = driver.find_element(By.PARTIAL_LINK_TEXT, "Form")
print("Form link is present. Clicking...")
time.sleep(2)   
form_link.click()
print("Clicked on the 'Form' link.")

# Verify the heading
heading = wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1"))).text
assert "Form" in heading
print(f"Heading verified: {heading}")

# Fill out the form
time.sleep(2)
driver.find_element(By.ID, "first-name").send_keys("John")
driver.find_element(By.ID, "last-name").send_keys("Doe")
driver.find_element(By.ID, "job-title").send_keys("Software Engineer")
print("Text fields filled successfully.")

    # Select radio button and checkbox
driver.find_element(By.XPATH, "//input[@value='radio-button-1']").click()
driver.find_element(By.XPATH, "//input[@value='checkbox-1']").click()
print("Radio button and checkbox selected.")

    # Select from dropdown
dropdown = driver.find_element(By.ID, "select-menu")
dropdown.click()
wait.until(EC.element_to_be_clickable((By.XPATH, "//option[@value='2']"))).click()
print("Dropdown value selected.")

    # Pick a date
date_input = driver.find_element(By.ID, "datepicker")
date_input.click()
driver.execute_script("window.scrollTo(0, 500);")

    # A more general way to select a date (e.g., today's date)
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".today.day"))).click()
print("Date picked successfully.")

print("Form filled successfully.")

driver.quit()