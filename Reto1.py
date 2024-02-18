import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common import TimeoutException

driver = webdriver.Chrome(executable_path="C:\Chromedriver\chromedriver.exe")
driver.get("https://demo.seleniumeasy.com/input-form-demo.html")
driver.maximize_window()
driver.implicitly_wait(5)

driver.find_element(By. XPATH, "//input[contains(@name,'first_name')]").send_keys("Franco" + Keys.TAB + "Perez" + Keys.TAB + "frnu@gmail.com" + Keys.TAB + "11382662777" + Keys.TAB + "Cagua la bella" + Keys.TAB + "Ciudad de Mexico")
time.sleep(3)
driver.execute_script("window.scrollTo(0,500)")
time.sleep(2)
ciudades = driver.find_element(By. XPATH, "//select[contains(@name,'state')]")
ciudad = Select(ciudades)
ciudad.select_by_index(4)

time.sleep(2)
driver.find_element(By. XPATH,"//input[contains(@name,'zip')]").send_keys("16764" + Keys.TAB + "www.google.com.ar")
time.sleep(2)


btn1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[contains(@value,'yes')]")))
btn1.click()
time.sleep(2)

driver.find_element(By. XPATH,"//textarea[contains(@class,'form-control')]").send_keys("esto esta ok mas finooo" + Keys.TAB + Keys.ENTER)
time.sleep(5)

