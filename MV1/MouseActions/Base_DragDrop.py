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
        f.Navegar("https://testpages.herokuapp.com/styled/drag-drop-javascript.html", t)

        #f.MouseClickDer("id", "rightClickBtn", 3)
        f.MouseDragDrop("xpath", "(//p[contains(.,'Drag me')])[1]", "(//p[contains(.,'Drop here')])[1]", 3)