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


@pytest.mark.validarif
def test_validarIF():
    a = 20
    b = 25

    if a == b:
        assert True, "Los datos son iguales"
    else:
        assert False, "No son iguales"