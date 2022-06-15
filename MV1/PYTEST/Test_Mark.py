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


@pytest.mark.run
def test_uno():
    print("Test uno")


@pytest.mark.run
def test_dos():
    print("Test dos")


@pytest.mark.run
def test_tres():
    print("Test tres")


@pytest.mark.notrun
def test_cuatro():
    print("Test cuatro")


@pytest.mark.notrun
def test_cinco():
    print("Test cinco")


@pytest.mark.run
def test_seis():
    print("Test seis")


@pytest.mark.skip
def test_siete():
    print("Test siete")