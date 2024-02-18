import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common import TimeoutException

class base_test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:\Chromedriver\chromedriver.exe")
        t=2
    
    def test1(self):
        driver = self.driver
        driver.get("https://demoqa.com/text-box")
        driver.maximize_window()
        time.sleep(4)

    def tearDown(self):
        driver = self.driver
        driver.close()

if __name__=='__main__':
    unittest.main()
