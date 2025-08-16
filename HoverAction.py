from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

# Set up headless options
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Create the WebDriver instance
driver = webdriver.Chrome(options=chrome_options)

driver.maximize_window()

driver.get("https://shop.qaautomationlabs.com/index.php")

hoverElement=driver.find_element(By.XPATH,"//a[text()='Shop ']")

time.sleep(2)
actions=ActionChains(driver)

actions.move_to_element(hoverElement).perform()

hoveredElement=driver.find_element(By.XPATH,"//a[text()='Womens Wear']")
hoveredElement.click()

driver.close()
