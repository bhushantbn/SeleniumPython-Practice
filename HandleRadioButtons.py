import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver=webdriver.Chrome()
driver.get("https://testing.qaautomationlabs.com/radio-button.php")

driver.execute_script("window.scrollBy(0,500);")
time.sleep(2)
link=driver.find_element(By.LINK_TEXT,"Radio Button")

link.click()
time.sleep(2)
radiobuttons=driver.find_elements(By.XPATH,"//input[@type='radio']")
disabled_count=sum(1 for rb in radiobuttons if not rb.is_enabled())
#lengthCount=len(disabled_count)
print(f"Total radio buttons: {len(radiobuttons)}")
print(f"Disabled radio buttons: {disabled_count}")

# Print each radio item text
for i, rb in enumerate(radiobuttons, start=1):
    label_text = rb.find_element(By.XPATH, "./parent::label").text
    print(f"{i}. {label_text} - {'Disabled' if not rb.is_enabled() else 'Enabled'}")


#assert radiobutton.is_displayed() is True,"Assertion failed.."

print("passed.")
driver.close()

