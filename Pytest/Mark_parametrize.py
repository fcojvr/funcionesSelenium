import pytest
import time
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
from selenium.webdriver.chrome.service import Service
current_directory = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_directory, "Funciones2"))
sys.path.append("C:/Users/fpaez/OneDrive - DXC Production/Documents/Selenium/CursoUdemy/Mouse_actions/Funciones2")
from Funciones2 import Funciones_Globales1
from Page_login import Funciones_Login
service = Service("C:/Chromedriver/chromedriver.exe")

def get_Data():
    return [
            ("francisc", "12233"),
            ("frans", "3332"),
            ("Admin", "admin123") ]

tg = 1

@pytest.mark.login  
@pytest.mark.parametrize("user, clave", get_Data())
def test_login(user, clave):
    global driver
    driver = webdriver.Chrome(service=service)
    f = Funciones_Globales1(driver)
    f.Navegar("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login", tg)
    driver.implicitly_wait(15)
    f.text_xpath_val("xpath","//input[contains(@class,'oxd-input oxd-input--focus')]",user, tg)
    f.text_xpath_val("xpath","//input[contains(@type,'password')]",clave, tg)
    f.click_xpath_val("xpath","//button[@type='submit'][contains(.,'Login')]", tg)
    print("Entrando al sistema dos...")
    
def teardown_function():
    print("Saliendo del sistema")
    driver.quit()