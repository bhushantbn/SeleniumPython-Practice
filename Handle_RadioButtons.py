import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

# Set up headless options
chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 20)

driver.get("https://shop.qaautomationlabs.com/index.php")
print(driver.title)
print(driver.current_url)

# Click Testing link
link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Testing']")))
link.click()

# Switch to new tab
driver.switch_to.window(driver.window_handles[-1])
print(driver.title)
print(driver.current_url)

# Important — wait until the Test site finishes loading
#wait.until(EC.title_contains("Testing"))

# Now click the “Radio Button” block once it’s visible
radio_button_block = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//p[normalize-space()='Radio Button']"))
)
radio_button_block.click()

print(driver.current_url)

assert "Radio Button" in driver.title, "Title does not contain 'Radio Button'"

print(f"test passed. {driver.title}")

driver.quit()
