import time
import os
import sys
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
current_directory = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_directory, "Funciones2"))
sys.path.append("C:/Users/fpaez/OneDrive - DXC Production/Documents/Selenium/CursoUdemy/Mouse_actions/Funciones2")
from Funciones2 import Funciones_Globales1
service = Service("C:/Chromedriver/chromedriver.exe")

class Funciones_Login():
    def __init__(self,driver):
        self.driver = driver

    def L1(self, email, clave, mensaje, t = .1):
        driver = webdriver.Chrome(service=service)
        f = Funciones_Globales1(driver)
        f.Navegar("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F", 1)
        f.text_xpath_val("xpath", "//input[contains(@id,'Email')]", email, 1)
        f.text_xpath_val("xpath", "//input[contains(@id,'Password')]", clave, 1)
        f.click_xpath_val("xpath", "//button[@type='submit'][contains(.,'Log in')]", 2)
        e1=f.SX("//li[contains(.,'No customer account found')]")
        e1= e1.text
        if(e1==mensaje):
            print("Prueba extiosa")
        else:
            print("Prueba fallida")
        driver.close()

    def L2(self, email, clave, mensaje, t = .1):
        driver = webdriver.Chrome(service=service)
        f = Funciones_Globales1(driver)
        f.Navegar("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F", 1)
        f.text_xpath_val("xpath", "//input[contains(@id,'Email')]", email, 1)
        f.text_xpath_val("xpath", "//input[contains(@id,'Password')]", clave, 1)
        f.click_xpath_val("xpath", "//button[@type='submit'][contains(.,'Log in')]", 2)
        e1=f.SX("//span[@id='Email-error']")
        e1= e1.text
        if(e1==mensaje):
            print("Prueba extiosa mensaje correcto")
        else:
            print("Prueba fallida")
        driver.close()
    
    def L3(self, email, clave, mensaje, t = .1):
        driver = webdriver.Chrome(service=service)
        f = Funciones_Globales1(driver)
        f.Navegar("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F", 2)
        f.text_xpath_val("xpath", "//input[contains(@id,'Email')]", email, 2)
        f.text_xpath_val("xpath", "//input[contains(@id,'Password')]", clave, 2)
        f.click_xpath_val("xpath", "//button[@type='submit'][contains(.,'Log in')]", 3)
        e1=f.SX("//h1[contains(.,'Dashboard')]")
        e1=e1.text
        if(e1== mensaje):
            print("Pruena exitosa mensjae correcto")
        else:
            print("Fallamos jefe")
        driver.close()
        
