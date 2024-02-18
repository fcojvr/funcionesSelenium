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

def test_login1():
    global driver
    driver = webdriver.Chrome(service=service)
    fl = Funciones_Login(driver)
    fl.L1("fco@gmail.com", "1223", "No customer account found")
    fl.L2("","1223","Please enter your email")
    fl.L3("admin@yourstore.com", "admin", "Dashboard")
    


