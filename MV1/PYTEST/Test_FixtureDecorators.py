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
from Funciones_PageLogin import FuncionesLogin
from selenium.webdriver import ActionChains

t = 1
driver = ""
f = ""


def setup_function(function):
    global driver, f
    driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
    driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
    driver.maximize_window()
    f = FuncionesGlobales(driver)
    f.TextoMixto("id", "Email", "admin@yourstore.com", t)
    f.TextoMixto("id", "Password", "admin", t)
    f.ClickMixto("xpath", "//button[@type='submit'][contains(.,'Log in')]", t)
    print("\nIniciando nuestro test")


def teardown_function(function):
    print("Fin de los test\n")
    driver.close()


def test_uno():
    f.ClickMixto("xpath", "//a[@href='#'][contains(.,'Catalog')]", t)
    f.ClickMixto("xpath", "(//p[contains(.,'Products')])[1]", t)
    f.TextoMixto("id", "SearchProductName", "Computer", t)
    f.ClickMixto("id", "search-products", t)


def test_dos():
    #driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
    #f = FuncionesGlobales(driver)
    f.ClickMixto("xpath", "//a[@href='#'][contains(.,'Catalog')]", t)
    f.ClickMixto("xpath", "(//p[contains(.,'Products')])[1]", t)
    f.ClickMixto("xpath", "//i[contains(@class,'fas fa-plus-square')]", t)
    f.TextoMixto("id", "Name", "Dell", t)
    f.TextoMixto("id", "ShortDescription", "Laptop Gamer", t)
    #driver.switch_to.frame(0)
    #f.TextoMixto("id", "tinymce", "Laptop dell g5 16 gb ram", t)
    f.TextoMixto("xpath", "//input[contains(@id,'Sku')]", "12431241", t)
    #campo = driver.find_element(By.ID, "tinymce")
    #campo.send_keys("Laptop dell g5 16 gb ram" + Keys.TAB + "st123444")
    #time.sleep(t)