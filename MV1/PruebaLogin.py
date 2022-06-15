import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException

import BaseUnittest


class pruebaLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
        self.driver.maximize_window()

    def test_login1(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        nombre = driver.find_element(By.XPATH, "//input[contains(@id,'user-name')]")
        contraseña = driver.find_element(By.XPATH, "//input[contains(@id,'password')]")
        boton = driver.find_element(By.XPATH, "//input[contains(@id,'login-button')]")

        nombre.send_keys("Hugo")
        contraseña.send_keys("123")
        boton.click()

        error = driver.find_element(By.XPATH, "//h3[contains(@data-test,'error')]")
        error = error.text
        #print(error.text)

        if error == "Epic sadface: Username and password do not match any user in this service":
            print("Los datos no son correctos")

        time.sleep(2)

    def test_login2(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        nombre = driver.find_element(By.XPATH, "//input[contains(@id,'user-name')]")
        contraseña = driver.find_element(By.XPATH, "//input[contains(@id,'password')]")
        boton = driver.find_element(By.XPATH, "//input[contains(@id,'login-button')]")

        nombre.send_keys("")
        contraseña.send_keys("123")
        boton.click()

        error = driver.find_element(By.XPATH, "//h3[contains(@data-test,'error')]")
        error = error.text
        #print(error)

        if error == "Epic sadface: Username is required":
            print("Falta el nombre")

        time.sleep(2)

    def test_login3(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        nombre = driver.find_element(By.XPATH, "//input[contains(@id,'user-name')]")
        contraseña = driver.find_element(By.XPATH, "//input[contains(@id,'password')]")
        boton = driver.find_element(By.XPATH, "//input[contains(@id,'login-button')]")

        nombre.send_keys("Hugo")
        contraseña.send_keys("")
        boton.click()

        error = driver.find_element(By.XPATH, "//h3[contains(@data-test,'error')]")
        error = error.text
        #print(error)

        if error == "Epic sadface: Password is required":
            print("Falta la contraseña")

        time.sleep(2)

    def test_login4(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        nombre = driver.find_element(By.XPATH, "//input[contains(@id,'user-name')]")
        contraseña = driver.find_element(By.XPATH, "//input[contains(@id,'password')]")
        boton = driver.find_element(By.XPATH, "//input[contains(@id,'login-button')]")

        nombre.send_keys("")
        contraseña.send_keys("")
        boton.click()

        error = driver.find_element(By.XPATH, "//h3[contains(@data-test,'error')]")
        error = error.text
        #print(error)

        if error == "Epic sadface: Username is required":
            print("Faltan los 2 campos")

        time.sleep(2)

    def test_login5(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        nombre = driver.find_element(By.XPATH, "//input[contains(@id,'user-name')]")
        contraseña = driver.find_element(By.XPATH, "//input[contains(@id,'password')]")
        boton = driver.find_element(By.XPATH, "//input[contains(@id,'login-button')]")

        nombre.send_keys("standard_user")
        contraseña.send_keys("secret_sauce")
        boton.click()

        elemento = driver.find_element(By.XPATH, "//span[@class='title'][contains(.,'Products')]")
        print(elemento.is_enabled())

        if elemento.is_enabled():
            print("Inicio de sesion exitoso")

        time.sleep(2)

    def tearDown(self):
        driver = self.driver
        driver.close()

if __name__ == "__main__":
    unittest.main()