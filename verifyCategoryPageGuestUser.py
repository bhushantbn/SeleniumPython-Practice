import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Headless Chrome setup
chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--window-size=1920,1080")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)
wait = WebDriverWait(driver, 20)
driver.maximize_window()

driver.get("https://shop.qaautomationlabs.com/index.php")

# Locate the "Shop" menu
shop_menu = driver.find_element(By.XPATH, "//a[normalize-space()='Shop']")

# Reveal the dropdown using JS (toggle visibility + hover classes if necessary)
driver.execute_script("""
arguments[0].classList.add('show'); 
arguments[0].nextElementSibling.classList.add('show');
""", shop_menu)

time.sleep(1)  # small delay to ensure JS changes take effect

# Click "Womens Wear" via JS directly (bypasses headless interactivity issues)
womens_wear_link = driver.find_element(By.XPATH, "//a[normalize-space()='Womens Wear']")
driver.execute_script("arguments[0].click();", womens_wear_link)

# Example assertion
time.sleep(2)
assert "This Page Does Not Exist" in driver.title, "Assertion failed: unexpected title"
print("Pass. Title:", driver.title)

driver.quit()
