from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

driver.get("https://testing.qaautomationlabs.com/radio-button.php")

# scroll down so radio buttons are visible
driver.execute_script("window.scrollBy(0, 500);")

wait = WebDriverWait(driver, 20)

# find all radio buttons
radiobuttons = driver.find_elements(By.XPATH, "//input[@type='radio']")

disabled_count = sum(1 for rb in radiobuttons if not rb.is_enabled())

print(f"Total radio buttons: {len(radiobuttons)}")
print(f"Disabled radio buttons: {disabled_count}")

# print each radio button with its label text
for i, rb in enumerate(radiobuttons, start=1):
    label_text = rb.find_element(By.XPATH, "./parent::label").text
    print(f"{i}. {label_text} - {'Disabled' if not rb.is_enabled() else 'Enabled'}")

print("passed.")
driver.close()
