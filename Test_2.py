import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path="C:\Chromedriver\chromedriver.exe")

driver.get("https://demo.seleniumeasy.com/basic-checkbox-demo.html")
driver.maximize_window()
driver.implicitly_wait(10)
time.sleep(2)

btn1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//input[contains(@type,'checkbox')])[1]")))
btn1.click()
time.sleep(3)

btn2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//input[contains(@type,'checkbox')])[5]")))
btn2.click()
time.sleep(3)
