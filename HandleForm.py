from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# -----------------------------
# Setup headless Chrome options
# -----------------------------
chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--window-size=1920,1080")

# Setup WebDriver service
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)
wait = WebDriverWait(driver, 20)

# Maximize window (optional)
driver.maximize_window()

# -----------------------------
# Navigate to Formy Project home
# -----------------------------
driver.get("https://formy-project.herokuapp.com/")
print("Navigated to the home page.")

# Click on "Form" link
form_link = wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Form")))
form_link.click()
print("Clicked on the 'Form' link.")

# -----------------------------
# Wait for heading to load
# -----------------------------
heading_element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
heading = heading_element.text
assert "Form" in heading, f"Expected 'Form' in heading but got '{heading}'"
print(f"Heading verified: {heading}")

# -----------------------------
# Fill out the text fields
# -----------------------------
wait.until(EC.presence_of_element_located((By.ID, "first-name"))).send_keys("John")
driver.find_element(By.ID, "last-name").send_keys("Doe")
driver.find_element(By.ID, "job-title").send_keys("Software Engineer")
print("Text fields filled successfully.")

# -----------------------------
# Select radio button and checkbox
# -----------------------------
driver.find_element(By.XPATH, "//input[@value='radio-button-1']").click()
driver.find_element(By.XPATH, "//input[@value='checkbox-1']").click()
print("Radio button and checkbox selected.")

# -----------------------------
# Select a value from dropdown
# -----------------------------
dropdown = driver.find_element(By.ID, "select-menu")
dropdown.click()
wait.until(EC.element_to_be_clickable((By.XPATH, "//option[@value='2']"))).click()
print("Dropdown value selected.")

# -----------------------------
# Pick a date
# -----------------------------
date_input = driver.find_element(By.ID, "datepicker")
date_input.click()

# Scroll if needed
driver.execute_script("window.scrollTo(0, 500);")

# Click today's date
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".today.day"))).click()
print("Date picked successfully.")

# -----------------------------
# Form submission (optional)
# -----------------------------
# driver.find_element(By.XPATH, "//a[text()='Submit']").click()
# print("Form submitted.")

print("Form filled successfully in headless CI mode.")

# -----------------------------
# Quit the driver
# -----------------------------
driver.quit()
