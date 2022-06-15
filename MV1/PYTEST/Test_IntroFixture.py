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


def setup_function(function):
    print("\nEsto va al inicio de cada test")


def teardown_function(function):
    print("Esto va al final de cada test\n")


def test_uno():
    print("Test uno")


def test_dos():
    print("Test dos")


def test_tres():
    print("Test tres")


def test_cuatro():
    print("Test cuatro")