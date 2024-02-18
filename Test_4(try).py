import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common import TimeoutException

driver = webdriver.Chrome(executable_path="C:\Chromedriver\chromedriver.exe")

driver.get("https://demo.seleniumeasy.com/basic-select-dropdown-demo.html")
driver.maximize_window()
driver.implicitly_wait(10)

try:
    diasSelect = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//select[contains(@id,'select-demo0')]")))
    ds=Select(diasSelect)
    ds.select_by_visible_text("Sunday")
    time.sleep(1)
    ds.select_by_index(3)
    time.sleep(1)
    ds.select_by_value("Saturday")
    time.sleep(1)
except TimeoutException as ex:
    print(ex.msg)
    print("elemento no disponible")

    
driver.execute_script("window.scrollTo(0,400)")
time.sleep(1)
ciudades= Select(driver.find_element(By.ID, "multi-select"))
ciudades.select_by_index(2)
time.sleep(2)

ciudades.select_by_index(5)
time.sleep(2)
