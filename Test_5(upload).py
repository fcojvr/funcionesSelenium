import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common import TimeoutException

driver = webdriver.Chrome(executable_path="C:\Chromedriver\chromedriver.exe")

driver.get("https://testpages.eviltester.com/styled/file-upload-test.html")
driver.maximize_window()
driver.implicitly_wait(10)
t=1

try:
    Buscar = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//input[contains(@id,'fileinput')]")))
    Buscar = driver.find_element(By.XPATH, "//input[contains(@id,'fileinput')]")
    Buscar.send_keys("C://CursoSeleniumJava//boat-8123031_1280.jpg")
    time.sleep(t)
    driver.find_element(By.XPATH, "//input[contains(@id,'itsanimage')]").click()
    driver.find_element(By.XPATH, "//input[contains(@type,'submit')]").click()
    time.sleep(t)
except TimeoutException as ex:
    print(ex.msg)
    print("elemento no disponible")

    
time.sleep(t)
