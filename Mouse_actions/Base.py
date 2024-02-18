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
from selenium.webdriver import ActionChains

current_directory = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_directory, "Funciones2"))
sys.path.append("C:/Users/fpaez/OneDrive - DXC Production/Documents/Selenium/CursoUdemy/Mouse_actions/Funciones2")
from Funciones2 import Funciones_Globales1



tg=1.5
class base_test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:\Chromedriver\chromedriver.exe")
        t=2
    
    def test1(self):
        driver = self.driver
        f = Funciones_Globales1(driver)
        f.Navegar("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login",tg)
        f.text_xpath_val("//input[contains(@class,'oxd-input oxd-input--focus')]","Admin", tg)
        f.text_xpath_val("//input[contains(@type,'password')]","admin123", tg)
        f.click_xpath_val("//button[@type='submit'][contains(.,'Login')]", 4)

    
        admi= driver.find_element(By.XPATH, "(//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'])[1]")
        sub1 = driver.find_element(By.XPATH, "(//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'])[1]")
        act = ActionChains(driver)
        act = act.move_to_element(admi).move_to_element(sub1).click().perform()
        time.sleep(3)
                   




    def tearDown(self):
        driver = self.driver
        driver.close()

if __name__=='__main__':
    unittest.main()