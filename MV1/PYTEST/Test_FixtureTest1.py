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
def setup_login_uno():
    print("\nEmpezando login del sistema uno")
    yield
    print("Saliendo del sistema uno, prueba ok")


@pytest.fixture(scope='module')
def setup_login_dos():
    print("\nEmpezando login del sistema dos")
    yield
    print("Saliendo del sistema dos, prueba ok")


def test_uno(setup_login_uno):
    print("\nEmpezando las pruebas del test uno")


def test_dos(setup_login_dos):
    print("\nEmpezando las pruebas del test dos")


@pytest.mark.usefixtures("setup_login_dos")
def test_tres():
    print("\nPrueba tres del modulo login dos")