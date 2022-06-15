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
from Funciones_PageLogin import FuncionesLogin

t = 1
global driver


def test_login1():
    driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
    fl = FuncionesLogin(driver)
    fl.login1("admin@yourstore.com", "admin", "Existe", t)      #Email y contra correctas
    fl.login2("", "1234", "Please enter your email", t)         #Falta el Email
    fl.login3("hugo", "pass", "Wrong email", t)                 #Email incompleto
