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
from selenium.webdriver import ActionChains

t=1

class base_Test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
        self.driver.maximize_window()

    def test1(self):
        driver = self.driver
        f = FuncionesGlobales(driver)
        f.Navegar("https://www.google.com/webhp?hl=es&sa=X&ved=0ahUKEwjj6vaWjJf4AhXylOAKHQ-8CD8QPAgI", t)

        f.TextoMixto("xpath", "(//input[contains(@aria-label,'Buscar')])[1]", "Fer", 4)
        f.MouseClickXY("xpath", "(//input[contains(@aria-label,'Buscar')])[1]", "0", "250", t)

        #f.MouseClickXY("xpath", "//a[@href='https://jqueryui.com/demos/'][contains(.,'Demos')]", "350", "0", 4)