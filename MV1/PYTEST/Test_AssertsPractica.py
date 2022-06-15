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


@pytest.fixture(scope='module')
def setup_Login():
    global driver, f
    driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
    driver.get("https://opensource-demo.orangehrmlive.com/")
    driver.maximize_window()
    driver.implicitly_wait(20)
    f = FuncionesGlobales(driver)
    f.TextoMixto("id", "txtUsername", "Admin", t)
    f.TextoMixto("id", "txtPassword", "admin123", t)
    f.ClickMixto("id", "btnLogin", t)
    print("\nEntrando al sistema login dos")


def teardown_function():
    print("\nFin de todos los test")
    driver.close()


@pytest.mark.login
@pytest.mark.usefixtures("setup_Login")
def test_uno():
    f = FuncionesGlobales(driver)
    etiqueta = f.SelElemXpath("//h1[contains(.,'Dashboard')]").text
    print(etiqueta)
    if etiqueta == "Dashboard":
        print("Adentro")
        assert etiqueta == "Dashboard"
    else:
        print("Afuera")
        assert etiqueta != "Dashboard", "No estas en la pagina de inicio"


    #assert etiqueta == "Dashboard", "No pudiste entrar al sistema"