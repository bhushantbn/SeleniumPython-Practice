from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()

driver.maximize_window()
driver.get("https://facebook.com")

# Open first new tab
driver.execute_script("window.open('https://www.wikipedia.org', '_blank');")
time.sleep(1)

# Open second new tab
driver.execute_script("window.open('https://www.python.org', '_blank');")
time.sleep(1)

# Get all window handles
handles = driver.window_handles

# Switch to 2nd tab (Wikipedia)
driver.switch_to.window(handles[1])
print("Now in tab 2:", driver.title)

# Switch to 3rd tab (Python)
driver.switch_to.window(handles[2])
print("Now in tab 3:", driver.title)

# Switch back to original tab
driver.switch_to.window(handles[0])
print("Back to original tab:", driver.title)

driver.quit()
