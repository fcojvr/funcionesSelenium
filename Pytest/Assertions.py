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

@pytest.fixture(scope='module')
def setup_login():
    global driver
    driver = webdriver.Chrome(service=service)
    f = Funciones_Globales1(driver)
    f.Navegar("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login", 3)
    driver.implicitly_wait(20)
    f.text_xpath_val("xpath","//input[contains(@name,'username')]","Admin", 2)
    f.text_xpath_val("xpath","//input[contains(@name,'password')]","admin123", 2)
    f.click_xpath_val("xpath","//button[@type='submit'][contains(.,'Login')]", 3)
    print("Entrando al sistema...")
    return f
def teardown_function():
    print("Saliendo del test")
    driver.close()


@pytest.mark.login  
@pytest.mark.usefixtures("setup_login")
def test_uno(setup_login):
    f = setup_login
    etiqueta = f.SX("//h6[contains(.,'Dashboard')]").text
    if etiqueta == "Dashboar":
            print("Dentro del sistema")
            assert etiqueta == "Dashboar"
    else:
            print("Afuera del sistema")
            assert etiqueta == "Dashboar", "No entraste" 



