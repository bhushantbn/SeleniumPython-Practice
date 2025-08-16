from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
driver.get("https://shop.qaautomationlabs.com/index.php")

wait = WebDriverWait(driver, 10)

# Click link that opens new tab
driver.find_element(By.XPATH, "//a[text()='Testing']").click()

# Switch to the newly opened tab
driver.switch_to.window(driver.window_handles[-1])

# Click the hamburger menu
menu_button = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//a[@class='nav-link' and @data-toggle='dropdown']"))
)

menu_button.click()

# Small delay for animation
time.sleep(1)

# Wait for <a class="dropdown-item"> elements inside the dropdown
menu_items = driver.find_elements(By.XPATH, "//div[contains(@class,'dropdown-menu') and contains(@class,'show')]//a[contains(@class,'dropdown-item')]")

time.sleep(1)


# Validate count

# Print each menu item text
for i, item in enumerate(menu_items, start=1):
    print(f"{i}. {item.text}")

assert len(menu_items) == 8, f"Expected 8 menu items, but found {len(menu_items)}"
print("assertion passed.")
# print("✅ All 8 menu items are visible after clicking the menu button.")

driver.quit()
