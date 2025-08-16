from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options

# Set up headless options
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Create the WebDriver instance
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.google.com");

searchbox=driver.find_element(By.NAME,"q");
searchbox.send_keys("Selenium Python")
searchbox.send_keys(Keys.RETURN)

time.sleep(2);

print("page title is:",driver.title);

driver.quit()