from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# prepare headless options for CI
chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 20)

driver.get("https://shop.qaautomationlabs.com/index.php")

# Click Testing link
old_tabs = driver.window_handles
testing_link = wait.until(EC.element_to_be_clickable(
    (By.XPATH, "//a[normalize-space()='Testing']"))
)
testing_link.click()

# Wait for new tab to appear
wait.until(lambda d: len(d.window_handles) > len(old_tabs))

# Switch to the newly opened tab
driver.switch_to.window(driver.window_handles[-1])

# Now click the “CheckBox” card
checkbox_card = wait.until(EC.element_to_be_clickable((By.XPATH, "//p[normalize-space()='CheckBox']")))
checkbox_card.click()

# Click the toggle button and validate it
toggleBtn = wait.until(EC.element_to_be_clickable((By.ID, "toggleBtn")))
toggleBtn.click()
assert toggleBtn.text == "Uncheck All", "Toggle button text did not change"

print("Toggle assertion passed")

# Validate all checkboxes are selected
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
checked = [cb for cb in checkboxes if cb.is_selected()]
assert len(checked) == 4, f"Expected 4 selected, got {len(checked)}"

print("Checkbox Validation Passed ✅")

driver.quit()
