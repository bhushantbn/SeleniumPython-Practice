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

# Login
driver.find_element(By.ID,"email").send_keys("demo@demo.com")
driver.find_element(By.ID,"password").send_keys("demo")
driver.find_element(By.ID,"loginBtn").click()

expectedURL = "https://shop.qaautomationlabs.com/shop.php"
assert driver.current_url == expectedURL, "Login assertion failed"
print("Login passed")

time.sleep(2)

# Reveal the "Shop" dropdown via JavaScript
shop_menu = driver.find_element(By.XPATH, "//a[normalize-space()='Shop']")
driver.execute_script("""
arguments[0].classList.add('show'); 
arguments[0].nextElementSibling.classList.add('show');
""", shop_menu)

time.sleep(1)  # let JS changes apply

# Click "View All" link using JS (avoids headless hover issues)
view_all_link = driver.find_element(By.XPATH, "//a[normalize-space()='View All']")
driver.execute_script("arguments[0].click();", view_all_link)

time.sleep(2)

# Verify breadcrumb
breadcrumb = driver.find_element(By.XPATH,"//a[text()='Shop']")
assert breadcrumb.text == "Shop", "Breadcrumb assertion failed"
print("Breadcrumb verified:", breadcrumb.text)

time.sleep(2)
driver.quit()
