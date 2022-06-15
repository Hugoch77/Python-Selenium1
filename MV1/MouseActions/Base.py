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
        f.Navegar("https://opensource-demo.orangehrmlive.com/", t)

        f.TextoMixto("id", "txtUsername", "Admin", t)
        f.TextoMixto("id", "txtPassword", "admin123", t)
        f.ClickMixto("id", "btnLogin", t)

        admin = driver.find_element(By.ID, "menu_admin_viewAdminModule")
        submenu1 = driver.find_element(By.ID, "menu_admin_UserManagement")
        submenu2 = driver.find_element(By.ID, "menu_admin_viewSystemUsers")

        action = ActionChains(driver)

        action.move_to_element(admin).move_to_element(submenu1).move_to_element(submenu2).click().perform()