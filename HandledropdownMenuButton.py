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

driver.get("https://formy-project.herokuapp.com/")

# Navigate to Dropdown page
driver.find_element(By.LINK_TEXT, "Dropdown").click()
time.sleep(2)
# Use JS click to open dropdown
dropdown_button = driver.find_element(By.ID, "dropdownMenuButton")
driver.execute_script("arguments[0].click();", dropdown_button)
print("Clicked dropdown button via JS")

time.sleep(1)  # wait for menu animation

# Check if dropdown menu visible
dropdown_menu = driver.find_element(By.ID, "dropdownMenuButton")
print("Dropdown menu displayed:", dropdown_menu.is_displayed())

# Click option 'Action' via JS
time.sleep(2)
dropdown_option = driver.find_element(By.XPATH, "//a[text()='Buttons']")
driver.execute_script("arguments[0].click();", dropdown_option)
time.sleep(2)

visible_element=driver.find_element(By.XPATH,"//button[@class='btn btn-lg btn-primary']")

assert visible_element.is_displayed() is True,"Not displayed element"
btnGroupDropdown= driver.find_element(By.ID,"btnGroupDrop1")
assert btnGroupDropdown.is_displayed() is True, "Not visible element"
time.sleep(2)
btnGroupDropdown.click()
time.sleep(2)
assert driver.find_element(By.XPATH,"//a[text()='Dropdown link 2']").is_displayed() is True,"btnGroupDropdown values Not visible "

time.sleep(2)
print("dropdown assertion process complete")
driver.quit()
