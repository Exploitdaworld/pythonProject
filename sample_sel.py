from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

path=Service(r"C:\Users\moiza\PycharmProjects\pythonProject\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=path)
driver.get("https://www.saucedemo.com/")
driver.maximize_window()

driver = webdriver.Chrome(ChromeDriverManager().install())



while(True):
    pass

