import time
import unittest
import openpyxl

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from Funciones.Funciones import FuncionesGlobales
from Funciones.PageLogin import PaginaLogin
from FuncionesExl import *

t=1

class baseTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
        self.driver.maximize_window()

    def test1(self):
        driver = self.driver
        f = FuncionesGlobales(driver)
        fe = Funexcel(driver)
        f.Navegar("https://demoqa.com/text-box")
        ruta = "C://Users//Ing. Hugo//Desktop//Software pruebas//Python//EjercicioPython.xlsx"
        filas = fe.getRowCount(ruta, "Hoja1")

        for i in range(2, filas+1):
            nombre = fe.readData(ruta, "Hoja1", i, 1)
            email = fe.readData(ruta, "Hoja1", i, 2)
            dir1 = fe.readData(ruta, "Hoja1", i, 3)
            dir2 = fe.readData(ruta, "Hoja1", i, 4)

            f.TextoMixto("id", "userName", nombre, t)
            f.TextoMixto("id", "userEmail", email, t)
            f.TextoMixto("id", "currentAddress", dir1, t)
            f.TextoMixto("id", "permanentAddress", dir2, t)
            f.ClickMixto("id", "submit", t)

            e = f.ExisteMixto("id", "name", t)
            if e == "Existe":
                print("El numero se inserto correctamente")
                fe.writeData(ruta, "Hoja1", i, 5, "Insertado")
            else:
                print("No se Inserto")
                fe.writeData(ruta, "Hoja1", i, 5, "Error")