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
class base_test1(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:\Chromedriver\chromedriver.exe")
        t=2
    
    def test1(self):
        driver = self.driver
        f = Funciones_Globales1(driver)
        """""
        f.Navegar("https://demoqa.com/buttons",tg)
        
        elemento = driver.find_element(By. XPATH, "//button[contains(@id,'doubleClickBtn')]")
        
       
        act = ActionChains(driver)
        act = act.double_click(elemento).perform()
        time.sleep(3)
        
        f.Mouse_Derecho("id","rightClickBtn",3)
        
        f.Navegar("https://testpages.eviltester.com/styled/drag-drop-javascript.html", 3)
        f.Mouse_DragDrop("xpath", "//div[contains(@id,'draggable1')]","//div[contains(@id,'droppable1')]", 2)
        f.Mouse_DragDrop("xpath", "//div[contains(@id,'draggable2')]","//div[contains(@id,'droppable2')]", 2)
        
        f.Navegar("https://www.google.co.ve/?gws_rd=cr&ei=e7UeUvXGOoT48gTcnoCYAg",2)
        f.text_xpath_val("xpath","//textarea[@id='APjFqb']", "D", tg)
        f.ClickXY("xpath","//textarea[@id='APjFqb']", 0 , 180, 4)
        """
        f.Navegar("https://demoqa.com/automation-practice-form",2)
        f.text_xpath_val("xpath", "//input[contains(@id,'firstName')]","FRAN", 1)
        act = ActionChains(driver)
        act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
        time.sleep(2)
        act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()
        act.send_keys(Keys.TAB)
        act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
        act.send_keys(Keys.TAB)
        act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).send_keys("@gmail.com").perform()
        time.sleep(2)


    def tearDown(self):
        driver = self.driver
        driver.close()

if __name__=='__main__':
    unittest.main()