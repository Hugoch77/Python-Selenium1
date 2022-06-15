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

class PaginaLogin():

    def __init__(self, driver):
        self.driver = driver

    def loginMaster(self, url, name, pasw, t):
        driver = self.driver
        f = FuncionesGlobales(driver)
        f.Navegar(url, t)
        f.TextoXpathVal("//input[contains(@id,'user-name')]", name, t)
        f.TextoXpathVal("//input[contains(@id,'password')]", pasw, t)
        f.ClickXpathVal("//input[contains(@id,'login-button')]", t)
        f.Salida()