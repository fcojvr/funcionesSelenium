import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common import TimeoutException


class Funciones_Globales():
    def __init__(self,driver):
        self.driver = driver

    def Tiempo(self,tie):
        t=time.sleep(tie)
        return t
    
    def Navegar(self,url,tiempo):
        self.driver.get(url)
        self.driver.maximize_window()
        print("Page open:"+ url)
        t=time.sleep(tiempo)
        return t
    
    def text_xpath_val(self,xpath,texto,tiempo):
        try:
            val = WebDriverWait(self.driver,4).until(EC.visibility_of_element_located((By.XPATH,xpath)))
            val = self.driver.find_element(By.XPATH, xpath)
            val.clear()
            val.send_keys(texto)
            print("escribiendo en el campo: {} en el texto: {}".format(xpath,texto))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("elemento no encontrado:"+ xpath)
            
    def click_xpath_val(self,xpath,tiempo):
        try:
            val = WebDriverWait(self.driver,4).until(EC.visibility_of_element_located((By.XPATH,xpath)))
            val = self.driver.find_element(By.XPATH, xpath)
            val.click()
            print("click en el campo {}".format(xpath))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("elemento no encontrado:"+ xpath)

    def select_xpath_type(self,xpath,tipo,dato,tiempo):
        try:
            val= WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By. XPATH, xpath)))
            val= self.driver.find_element(By. XPATH, xpath)
            val= Select(val)
            if(tipo=="text"):
                val.select_by_visible_text(dato)
            elif(tipo=="value"):
                val.select_by_value(dato)
            elif(tipo=="index"):
                val.select_by_index(dato)
            print("El campo seleccionado es {}".format(dato))
            t= time.sleep(tiempo)
        except TimeoutException as ex:
            print(ex.msg)
            print("elemento no encontrado:"+ xpath)

    def upload_xpath(self,xpath,ruta,tiempo):
        try:
            val = WebDriverWait(self.driver,4).until(EC.visibility_of_element_located((By.XPATH,xpath)))
            val = self.driver.find_element(By.XPATH, xpath)
            val.send_keys(ruta)
            print("se carga imagen {}".format(ruta))
            t = time.sleep(tiempo)
        except TimeoutException as ex:
            print(ex.msg)
            print("elemento no encontrado:"+ xpath)

    def check_xpath(self,xpath,tiempo):
        try:
            val = WebDriverWait(self.driver,4).until(EC.visibility_of_element_located((By.XPATH,xpath)))
            val = self.driver.find_element(By.XPATH, xpath)
            val.click()
            print("click en el elemento {}".format(xpath))
            t = time.sleep(tiempo)
            return  t
        except TimeoutException as ex:
            print(ex.msg)
            print("elemento no encontrado:"+ xpath)

    def check_xpath_mult(self,tiempo, *args):
        try:
            for num in args:    
                val = WebDriverWait(self.driver,4).until(EC.visibility_of_element_located((By.XPATH,num)))
                val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
                val = self.driver.find_element(By.XPATH, num)
                val.click()
                print("click en el elemento {}".format(num))
                t = time.sleep(tiempo)
        except TimeoutException as ex:
            for num in args:
                print(ex.msg)
                print("elemento no encontrado:"+ num)

    def Existe(self,xpath,tiempo):
        try:
            val = WebDriverWait(self.driver,4).until(EC.visibility_of_element_located((By.XPATH,xpath)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
            val = self.driver.find_element(By.XPATH, xpath)
            val.click()
            print("El elemento {} -> Existe".format(xpath))
            t = time.sleep(tiempo)
            return "Existe"
        except TimeoutException as ex:
            print(ex.msg)
            print("elemento no existe:"+ xpath)        