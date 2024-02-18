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

from PageLogin import pagina_login

tg=2
class base_test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:\Chromedriver\chromedriver.exe")
        t=2
    
    def test1(self):
        driver = self.driver
        f=Funciones_Globales(driver)
        pg=pagina_login(driver)
        pg.login_master("https://www.saucedemo.com/","standard_user","secret_sauce",tg)
        f.select_xpath_type("//*[@id='header_container']/div[2]/div/span/select","index","1",tg)

    def tearDown(self):
        driver = self.driver
        driver.close()

if __name__=='__main__':
    unittest.main()