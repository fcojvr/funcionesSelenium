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
class base_test2(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:\Chromedriver\chromedriver.exe")
        t=2
    
    def test1(self):
        driver = self.driver
        f=Funciones_Globales(driver)
        f.Navegar("https://demo.seleniumeasy.com/basic-checkbox-demo.html",tg)
        for n in range(2,8):
            f.check_xpath_mult(3,"(//input[contains(@type,'checkbox')])["+str(n)+"]")


    def tearDown(self):
        driver = self.driver
        driver.close()

if __name__=='__main__':
    unittest.main()