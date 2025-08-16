from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options

# Set up headless options
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Create the WebDriver instance
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

driver.get("https://formy-project.herokuapp.com")

link = driver.find_element(By.LINK_TEXT, "Checkbox")
link.click()
print("Checkbox page opened.")
time.sleep(1)   
checkbox = driver.find_element(By.ID, "checkbox-1")
checkbox.click()
value=checkbox.get_attribute("value")
print("Checkbox value:", value)

time.sleep(1)
driver.quit()
