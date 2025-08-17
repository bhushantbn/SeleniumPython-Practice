from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

# Set up headless options
chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--window-size=1920,1080")  # critical for headless layout

# Create driver
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://shop.qaautomationlabs.com/shop.php")

wait = WebDriverWait(driver, 15)

# Click the "Testing" link which opens a new tab
link = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Testing']"))
)
link.click()

# Switch to the new tab
driver.switch_to.window(driver.window_handles[-1])

# Scroll up to ensure hamburger icon is in view
driver.execute_script("window.scrollTo(0, 0);")

# Click the hamburger menu button
menu_button = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//a[@class='nav-link' and @data-toggle='dropdown']"))
)
menu_button.click()

# Wait until dropdown menu is present AND visible
dropdown_locator = (
    By.XPATH,
    "//div[contains(@class,'dropdown-menu') and contains(@class,'show')]//a[contains(@class,'dropdown-item')]"
)

menu_items = wait.until(
    EC.visibility_of_all_elements_located(dropdown_locator)
)

# Print menu items
for i, item in enumerate(menu_items, start=1):
    print(f"{i}. {item.text}")

assert len(menu_items) == 8, f"Expected 8 menu items, but found {len(menu_items)}"
print("✅ Assertion passed. 8 menu items found.")

driver.quit()
