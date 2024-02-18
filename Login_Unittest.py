import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common import TimeoutException

class loginUnittest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:\Chromedriver\chromedriver.exe")
        t=2
    
    def test_Login1(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        nom = driver.find_element(By.XPATH, "//input[contains(@id,'user-name')]")
        clave = driver.find_element(By.XPATH, "//input[contains(@id,'password')]")
        btn = driver.find_element(By.XPATH,"//input[contains(@id,'login-button')]")
        nom.send_keys("hola")
        clave.send_keys("epa1")
        btn.click()
        error = driver.find_element(By.XPATH, "//h3[@data-test='error'][contains(.,'Epic sadface: Username and password do not match any user in this service')]")
        error = error.text
        print(error)
        time.sleep(4)
    
    def test_Login2(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        nom = driver.find_element(By.XPATH, "//input[contains(@id,'user-name')]")
        clave = driver.find_element(By.XPATH, "//input[contains(@id,'password')]")
        btn = driver.find_element(By.XPATH,"//input[contains(@id,'login-button')]")
        nom.send_keys("")
        clave.send_keys("epa1")
        btn.click()
        error = driver.find_element(By.XPATH, "//h3[@data-test='error'][contains(.,'Epic sadface: Username is required')]")
        error = error.text
        print(error)
        if(error=="Epic sadface: Username is required"):
            print("Falta el nombre")
            print("Prueba dos Ok")

    def test_Login3(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        nom = driver.find_element(By.XPATH, "//input[contains(@id,'user-name')]")
        clave = driver.find_element(By.XPATH, "//input[contains(@id,'password')]")
        btn = driver.find_element(By.XPATH,"//input[contains(@id,'login-button')]")
        nom.send_keys("standard_user")
        clave.send_keys("secret_sauce")
        btn.click()        
        elemento = driver.find_element(By. XPATH, "//img[@src='/static/media/bike-light-1200x1500.37c843b0.jpg']")
        elemento.is_displayed()
        print("El elemento es" + str(elemento))
        time.sleep(4)

    def tearDown(self):
        driver = self.driver
        driver.close()

if __name__=='__main__':
    unittest.main()