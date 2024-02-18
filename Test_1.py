import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path="C:\Chromedriver\chromedriver.exe")

driver.get("https://demoqa.com/text-box")
driver.maximize_window()
#driver.implicitly_wait(10)
time.sleep(2)

driver.find_element(By.XPATH, "//input[contains(@id,'userName')]").send_keys("Franco Perez" + Keys.TAB + "francoju@gmail.com" + Keys.TAB + "Calle 234" + Keys.TAB + "casa numero 8" + Keys.TAB + Keys.ENTER)
driver.execute_script("window.scrollTo(0,400)")

time.sleep(3)

driver.execute_script("window.scrollTo(400,0)")
driver.find_element(By.XPATH, "//li[contains(.,'Check Box')]").click()

time.sleep(3)
