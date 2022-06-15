import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from Funciones.Funciones import FuncionesGlobales
from Funciones.PageLogin import PaginaLogin

import BaseUnittest

t=0.5

class baseTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
        self.driver.maximize_window()

    def test1(self):
        driver = self.driver
        f = FuncionesGlobales(driver)
        f.Navegar("https://demoqa.com/text-box")
        #f.SelectXpathType("//select[contains(@id,'select-demo')]", "value", "Monday", t)
        #f.UploadXpath("//input[contains(@id,'fileinput')]", "C://Users//Ing. Hugo//PycharmProjects//CursoSelenium//Imagen//demo1.jpg", t)
        #f.CheckXpath("//input[contains(@id,'isAgeSelected')]", t)
        #for n in range(2, 6):
            #f.CheckXpathMultiple(t, "(//input[@type='checkbox'])["+str(n)+"]")
        f.TextoMixto("id", "userName", "Hugo", t)
        f.ClickMixto("id", "submit", t)

    def tearDown(self):
        driver = self.driver
        driver.close()

if __name__ == "__main__":
    unittest.main()