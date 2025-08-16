from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


driver=webdriver.Chrome();

driver.get("https://www.google.com");

searchbox=driver.find_element(By.NAME,"q");
searchbox.send_keys("Selenium Python")
searchbox.send_keys(Keys.RETURN)

time.sleep(2);

print("page title is:",driver.title);

driver.quit()