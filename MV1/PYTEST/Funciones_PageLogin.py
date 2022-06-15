import pytest
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from Funciones import FuncionesGlobales
from selenium.webdriver import ActionChains


class FuncionesLogin():

    def __init__(self, driver):
        self.driver = driver

    def login1(self, email, passw, mensaje, t):
        driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
        f = FuncionesGlobales(driver)
        f.Navegar("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F", t)
        driver.maximize_window()

        f.TextoMixto("id", "Email", email, t)
        f.TextoMixto("id", "Password", passw, t)
        f.ClickMixto("xpath", "//button[@type='submit'][contains(.,'Log in')]", t)
        validacion = f.ExisteMixto("xpath", "//h1[contains(.,'Dashboard')]", t)
        if validacion == mensaje:
            print("Prueba de login exitosa")
        else:
            print("Prueba de login no exitosa")

        driver.close()

    def login2(self, email, passw, mensaje, t):
        driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
        f = FuncionesGlobales(driver)
        f.Navegar("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F", t)
        driver.maximize_window()

        f.TextoMixto("id", "Email", email, t)
        f.TextoMixto("id", "Password", passw, t)
        f.ClickMixto("xpath", "//button[@type='submit'][contains(.,'Log in')]", t)
        e1 = f.SelElemXpath("//span[contains(@id,'Email-error')]")
        e1 = e1.text
        # print(e1)
        if e1 == mensaje:
            print("Prueba de email vacio exitosa")
        else:
            print("Prueba de email vacio no exitosa")

        driver.close()

    def login3(self, email, passw, mensaje, t):
        driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
        f = FuncionesGlobales(driver)
        f.Navegar("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F", t)
        driver.maximize_window()

        f.TextoMixto("id", "Email", email, t)
        f.TextoMixto("id", "Password", passw, t)
        f.ClickMixto("xpath", "//button[@type='submit'][contains(.,'Log in')]", t)
        e1 = f.SelElemXpath("//span[contains(@id,'Email-error')]")
        e1 = e1.text
        # print(e1)
        if e1 == mensaje:
            print("Prueba de email incompleto exitosa")
        else:
            print("Prueba de email incompleto no exitosa")

        driver.close()