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
def setup_login_uno():
    global driver, f
    driver = webdriver.Chrome(service=service)
    f = Funciones_Globales1(driver)
    f.Navegar("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F", 2)
    driver.implicitly_wait(15)
    f.text_xpath_val("xpath", "//input[contains(@id,'Email')]", "admin@yourstore.com", 1)
    f.text_xpath_val("xpath", "//input[contains(@id,'Password')]", "admin", 1)
    f.click_xpath_val("xpath", "//button[@type='submit'][contains(.,'Log in')]", 3)
    print("Entrando al sistema...")
    yield
    driver.quit()


@pytest.mark.usefixtures("setup_login_uno")
def test_uno():
    print("Entro al sistema uno")
    f.click_xpath_val("xpath","//a[@href='#'][contains(.,'Customers')]",1)
    f.click_xpath_val("xpath","(//p[contains(.,'Customers')])[2]",1)
    f.text_xpath_val("xpath","//input[contains(@id,'SearchFirstName')]","victoria",1)
    f.click_xpath_val("xpath","//button[contains(@id,'search-customers')]",1)
    f.click_xpath_val("xpath","//a[@href='/Admin/Customer/Create']",1)
    print("Creando empleado")
    email=driver.find_element(By. XPATH,"//input[contains(@id,'Email')]")
    email.send_keys("Fran@gmail.com" + Keys.TAB + "122333" + Keys.TAB + "Francisco" + Keys.TAB + "Paez")
    time.sleep(2)
    f.click_xpath_val("xpath","//input[contains(@id,'Gender_Male')]", 1)
    f.text_xpath_val("xpath","//input[contains(@id,'DateOfBirth')]", "12/10/1992", 1)
    print("Salida del login uno")
    

@pytest.fixture(scope='module')
def setup_login_dos():
    global driver, f
    driver = webdriver.Chrome(service=service)
    f = Funciones_Globales1(driver)
    f.Navegar("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login", 3)
    driver.implicitly_wait(15)
    f.text_xpath_val("xpath","//input[contains(@class,'oxd-input oxd-input--focus')]","Admin", 1)
    f.text_xpath_val("xpath","//input[contains(@type,'password')]","admin123", 1)
    f.click_xpath_val("xpath","//button[@type='submit'][contains(.,'Login')]", 3)
    print("Entrando al sistema dos...")
    yield
    print("Salida del login dos")
    driver.quit()

@pytest.mark.usefixtures("setup_login_dos")
def test_dos():
    print("Entro al sistema dos")
    f.click_xpath_val("xpath","//a[@href='/web/index.php/admin/viewAdminModule']",2)
    f.click_xpath_val("xpath","//span[@class='oxd-topbar-body-nav-tab-item'][contains(.,'User Management')]",2)
    f.click_xpath_val("xpath","(//li[contains(.,'Users')])[2]",3)
    #f.text_xpath_val("xpath","//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/input","Cheeku",2)
    #f.click_xpath_val("xpath","//button[@type='submit'][contains(.,'Search')]",2)
    
    
    

    
