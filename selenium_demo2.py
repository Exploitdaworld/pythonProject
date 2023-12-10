from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

time.sleep(5)
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
time.sleep(5)
#this is username section
myusername = driver.find_element(By.ID,"user-name")
myusername.send_keys("standard_user")

time.sleep(5)
#This is password section
mypassword= driver.find_element(By.ID,"password")
mypassword.send_keys("secret_sauce")

time.sleep(5)
#This is login section
mylogin = driver.find_element(By.ID,"login-button")
mylogin.click()




time.sleep(5)
#driver.quit()
