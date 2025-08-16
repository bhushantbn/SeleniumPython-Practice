import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://formy-project.herokuapp.com/fileupload")

# Create test file if not exists
file_name = "testfile.txt"
if not os.path.exists(file_name):
    with open(file_name, "w") as f:
        f.write("This is a test file for upload.")

# Build absolute file path
file_path = os.path.abspath(file_name)
print("Uploading file:", file_path)

# Send file path to the actual <input type="file">
driver.find_element(By.ID, "file-upload-field").send_keys(file_path)

# Wait to see the result
time.sleep(1)

# Assert file name appears in the text box
uploaded_text = driver.find_element(By.ID, "file-upload-field").get_attribute("value")
assert file_name in uploaded_text, f"Expected '{file_name}' in upload field, got '{uploaded_text}'"

print(file_name + " is the file name in the uploaded file.")
print("File uploaded successfully!")
driver.quit()
