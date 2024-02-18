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
from Funciones1 import Funciones_Globales
from Funciones_Ex import Funexcel


tg=.4
class base_test2(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:\Chromedriver\chromedriver.exe")
        t=2
    
    def test1(self):
        driver = self.driver
        f=Funciones_Globales(driver)
        fe = Funexcel(driver)
        f.Navegar("https://demoqa.com/text-box",tg)
        ruta = "C:/Users/fpaez/OneDrive - DXC Production/Documents/Selenium/CursoUdemy/Excel/Datos.xlsx"
        filas = fe.getRowCount(ruta, "Sheet1")
        
        for r in range (2, filas + 1):
            nombre = fe.readData(ruta,"Sheet1",r, 1)
            email = fe.readData(ruta, "Sheet1", r, 2)
            dir1 = fe.readData(ruta, "Sheet1", r, 3)
            dir2 = fe.readData(ruta, "Sheet1", r, 4)

            f.text_xpath_val("//input[contains(@id,'userName')]", nombre, tg)
            f.text_xpath_val("//input[contains(@id,'userEmail')]", email, tg)
            f.text_xpath_val("//textarea[contains(@id,'currentAddress')]", dir1, tg)
            f.text_xpath_val("//textarea[contains(@id,'permanentAddress')]", dir2, tg)
            f.click_xpath_val("//button[contains(@id,'submit')]", tg)

            e=f.Existe("//input[contains(@id,'userName')]", tg)
            if(e=="Existe"):
                print("El elemento se inserto correctamente")
                fe.writeData(ruta, "Sheet1", r, 5, "Insertado")
            else:
                print("No se inserto")
                fe.writeData(ruta, "Sheet1", r , "Error")

                        




    def tearDown(self):
        driver = self.driver
        driver.close()

if __name__=='__main__':
    unittest.main()