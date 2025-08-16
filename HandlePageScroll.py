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
driver.get("https://formy-project.herokuapp.com/")
driver.execute_script("window.scrollBy(0,500);")

link=driver.find_element(By.LINK_TEXT,"Page Scroll")
link.click()
time.sleep(2)
heading=driver.find_element(By.XPATH,"//h1[text()='Large page content']")



assert heading.is_displayed() is True,"Assertion failed.."

driver.execute_script("window.scrollBy(0,1000);")

time.sleep(2)

assert driver.find_element(By.ID,"name").is_displayed() is True,"Assertion failed.."
print("assertion1 passed..")
assert driver.find_element(By.ID,"date").is_displayed() is True,"Assertion failed.."
print("assertion2 passed..")


time.sleep(2)
driver.close()
