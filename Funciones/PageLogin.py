import time
import unittest
import os
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common import TimeoutException

current_directory = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_directory, "Funciones"))
sys.path.append("C:/Users/fpaez/OneDrive - DXC Production/Documents/Selenium/CursoUdemy/Funciones/Funciones")

from Funciones import Funciones_Globales
t=.3
class pagina_login():

    def __init__(self,driver):
        self.driver = driver
    
    def login_master(self,url,name,pas,t):
        driver = self.driver
        f=Funciones_Globales(driver)
        f.Navegar(url,t)
        f.text_xpath_val("//input[contains(@id,'user-name')]",name,t)
        f.text_xpath_val("//input[contains(@id,'password')]",pas,t)
        f.click_xpath_val("//input[contains(@id,'login-button')]",t)

    def tearDown(self):
        driver = self.driver
        driver.close()

if __name__=='__main__':
    unittest.main()