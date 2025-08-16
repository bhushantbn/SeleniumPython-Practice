from selenium import webdriver
import time
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

driver.get("https://formy-project.herokuapp.com/")
driver.execute_script("window.scrollBy(0,500);")
time.sleep(2)
link=driver.find_element(By.LINK_TEXT,"Switch Window")
link.click()
time.sleep(2)
driver.find_element(By.ID,"alert-button").click()
time.sleep(2)
try:
    alert=driver.switch_to.alert
    print("alert text:",alert.text)
    
    alert.accept()
    print("alert accepted.")
except:
    print("no alert present.")


driver.close()

