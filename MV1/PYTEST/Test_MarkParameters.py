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


def get_Data():
    return[
        ("Rodrigo", "1234"),
        ("Juan", "1234"),
        ("Pedro", "1234"),
        ("Hugo", "1234"),
        ("Admin", "admin123")
    ]


@pytest.mark.login
@pytest.mark.parametrize(("user", "clave"), get_Data())
def test_login(user, clave):
    global driver, f
    driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
    driver.get("https://opensource-demo.orangehrmlive.com/")
    driver.maximize_window()
    driver.implicitly_wait(20)
    f = FuncionesGlobales(driver)
    f.TextoMixto("id", "txtUsername", user, t)
    f.TextoMixto("id", "txtPassword", clave, t)
    f.ClickMixto("id", "btnLogin", t)
    print("\nEntrando al sistema login dos")


def teardown_function():
    print("Salida del test")
    driver.close()