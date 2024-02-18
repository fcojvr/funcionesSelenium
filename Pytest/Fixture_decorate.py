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
    print("Iniciando test...")
    yield
    print("Fin del test...")


@pytest.fixture(scope='module')
def setup_login_dos():
    print("Iniciando test dos...")
    yield
    print("Fin del test dos...")

def test_uno(setup_login_uno):
    print("-----Empezando test uno-----")

def test_dos(setup_login_dos):
    print("-----Empezando test dos dos dos dos-----")

@pytest.mark.usefixtures("setup_login_dos")
def test_tres():
    print("-----Empezando test 3 del login 2-----")
