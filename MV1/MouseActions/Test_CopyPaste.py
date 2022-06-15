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
        f.Navegar("https://demoqa.com/automation-practice-form", t)

        f.TextoMixto("xpath", "//input[contains(@id,'firstName')]", "Hugo", t)

        act = ActionChains(driver)
        act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
        time.sleep(2)
        act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()
        time.sleep(2)
        act.send_keys(Keys.TAB)
        act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
        time.sleep(2)
        act.send_keys(Keys.TAB)
        act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).send_keys("@gmail.com").perform()
        time.sleep(2)