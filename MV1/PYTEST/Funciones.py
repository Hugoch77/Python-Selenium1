import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains

class FuncionesGlobales():

    def __init__(self, driver):
        self.driver = driver

    #Funcion de tiempo
    def Tiempo(self, tiempo):
        t = time.sleep(tiempo)
        return t

    #Funcion para navegar
    def Navegar(self, Url, tiempo=0.1):
        self.driver.get(Url)
        print("Pagina abierta: " + str(Url))
        t = time.sleep(tiempo)
        return t

    def SelElemXpath (self, elemento):
        val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, elemento)))
        val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
        val = self.driver.find_element(By.XPATH, elemento)
        return val
    def SelElemID (self, elemento):
        val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, elemento)))
        val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
        val = self.driver.find_element(By.ID, elemento)
        return val

    #Funcion para introducir texto, ya se por xpath o id
    def TextoMixto (self, tipo, selector, texto, tiempo):
        try:
            if tipo == "xpath":
                val = self.SelElemXpath(selector)
                val.clear()
                val.send_keys(texto)
                print("\nEscribiendo en el campo {} el texto {}".format(selector, texto))
                t = time.sleep(tiempo)
                return t
            elif tipo == "id":
                val = self.SelElemID(selector)
                val.clear()
                val.send_keys(texto)
                print("\nEscribiendo en el campo {} el texto {}".format(selector, texto))
                t = time.sleep(tiempo)
                return t
        except TimeoutException as ex:
            print(ex.msg)
            print("\nNo se encontro el elemento" + selector)

    #Funcion para dar click por xpath o ID
    def ClickMixto (self, tipo, selector, tiempo):
        try:
            if tipo == "xpath":
                val = self.SelElemXpath(selector)
                val.click()
                print("\nDamos click en el campo {}".format(selector))
                t = time.sleep(tiempo)
                return t
            elif tipo == "id":
                val = self.SelElemID(selector)
                val.click()
                print("\nDamos click en el campo {}".format(selector))
                t = time.sleep(tiempo)
                return t
        except TimeoutException as ex:
            print(ex.msg)
            print("\nNo se encontro el elemento" + selector)

    def Salida(self):
        print("\nSe termina la prueba exitosamente")

    #Funcion para dropdowns
    def SelectXpathType (self, xpath, tipo, dato, tiempo):
        try:
            val = self.SelElemXpath(xpath)
            val = Select(val)
            if tipo == "text":
                val.select_by_visible_text(dato)
            elif tipo == "index":
                val.select_by_index(dato)
            elif tipo == "value":
                val.select_by_value(dato)
            print("\nEl campo seleccionado es {}".format(dato))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("\nNo se encontro el elemento" + xpath)

    #Funcion para subir archivos
    def UploadXpath (self, xpath, ruta, tiempo):
        try:
            val = self.SelElemXpath(xpath)
            val.send_keys(ruta)
            print("\nSe carga la imagen {}".format(ruta))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("\nNo se encontro el elemento" + xpath)

    #Funcion para Checkbox
    def CheckXpath (self, xpath, tiempo):
        try:
            val = self.SelElemXpath(xpath)
            val.click()
            print("\nSe da click en el elemento {}".format(xpath))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("\nNo se encontro el elemento" + xpath)

    #Funcion para multiples checkbox
    def CheckXpathMultiple (self, tiempo, *args):
        try:
            for num in args:
                val = self.SelElemXpath(num)
                val.click()
                print("\nSe da click en el elemento {}".format(num))
                t = time.sleep(tiempo)
                return t
        except TimeoutException as ex:
            for num in args:
                print(ex.msg)
                print("\nNo se encontro el elemento" + num)

    #Funcion para ver si un elmento existe
    def ExisteMixto (self, tipo, selector, tiempo):
        if tipo == "xpath":
            try:
                val = self.SelElemXpath(selector)
                print("\nEl elemento {} Existe".format(selector))
                t = time.sleep(tiempo)
                return "Existe"
            except TimeoutException as ex:
                print(ex.msg)
                print("\nNo se encontro el elemento" + selector)
                return "No Existe"
        elif tipo == "id":
            try:
                val = self.SelElemID(selector)
                print("\nEl elemento {} Existe".format(selector))
                t = time.sleep(tiempo)
                return "Existe"
            except TimeoutException as ex:
                print(ex.msg)
                print("\nNo se encontro el elemento" + selector)
                return "No Existe"

    #Funcion de mouse para dar doble click sobre un elemento
    def MouseDoble (self, tipo, selector, tiempo=.2):
        try:
            if tipo == "xpath":
                val = self.SelElemXpath(selector)
                action = ActionChains(self.driver)
                action.double_click(val).perform()
                print("\nDoble click en {}".format(selector))
                t = time.sleep(tiempo)
                return t
            elif tipo == "id":
                val = self.SelElemID(selector)
                action = ActionChains(self.driver)
                action.double_click(val).perform()
                print("\nDoble click en {}".format(selector))
                t = time.sleep(tiempo)
                return t
        except TimeoutException as ex:
            print(ex.msg)
            print("\nNo se encontro el elemento" + selector)

    # Funcion para dar click derecho
    def MouseClickDer (self, tipo, selector, tiempo=.2):
        try:
            if tipo == "xpath":
                val = self.SelElemXpath(selector)
                action = ActionChains(self.driver)
                action.context_click(val).perform()
                print("\nClick derecho en {}".format(selector))
                t = time.sleep(tiempo)
                return t
            elif tipo == "id":
                val = self.SelElemID(selector)
                action = ActionChains(self.driver)
                action.context_click(val).perform()
                print("\nClick derecho en {}".format(selector))
                t = time.sleep(tiempo)
                return t
        except TimeoutException as ex:
            print(ex.msg)
            print("\nNo se encontro el elemento" + selector)

    #Funcion para arrastrar y soltar objetos
    def MouseDragDrop (self, tipo, selector, destino, tiempo=.2):
        try:
            if tipo == "xpath":
                val = self.SelElemXpath(selector)
                val2 = self.SelElemXpath(destino)
                action = ActionChains(self.driver)
                action.drag_and_drop(val, val2).perform()
                print("\nselecciona el objeto {} y lo arrastra a {}".format(selector, destino))
                t = time.sleep(tiempo)
                return t
            elif tipo == "id":
                val = self.SelElemID(selector)
                val2 = self.SelElemID(destino)
                action = ActionChains(self.driver)
                action.drag_and_drop(val, val2).perform()
                print("\nselecciona el objeto {} y lo arrastra a {}".format(selector, destino))
                t = time.sleep(tiempo)
                return t
        except TimeoutException as ex:
            print(ex.msg)
            print("\nNo se encontro el elemento" + selector)

    #Funcion para arrastrar y soltar objetos en coordenadas XY
    def MouseDragDropXY (self, tipo, selector, x, y, tiempo=1):
        try:
            if tipo == "xpath":
                self.driver.switch_to.frame(0)
                val = self.SelElemXpath(selector)
                action = ActionChains(self.driver)
                action.drag_and_drop_by_offset(val, x, y).perform()
                print("\nArrastra el objeto {}".format(selector))
                t = time.sleep(tiempo)
                return t
            elif tipo == "id":
                self.driver.switch_to.frame(0)
                val = self.SelElemID(selector)
                action = ActionChains(self.driver)
                action.drag_and_drop_by_offset(val, x, y).perform()
                print("\nArrastra el objeto {}".format(selector))
                t = time.sleep(tiempo)
                return t
        except TimeoutException as ex:
            print(ex.msg)
            print("\nNo se encontro el elemento" + selector)

    #Funcion para dar click en coordenadas XY
    def MouseClickXY (self, tipo, selector, x, y, tiempo=1):
        try:
            if tipo == "xpath":
                #self.driver.switch_to.frame(0)
                val = self.SelElemXpath(selector)
                action = ActionChains(self.driver)
                action.move_to_element_with_offset(val, x, y).click().perform()
                print("\nClick al elemento {} coordenada {}, {}".format(selector, x, y))
                t = time.sleep(tiempo)
                return t
            elif tipo == "id":
                #self.driver.switch_to.frame(0)
                val = self.SelElemID(selector)
                action = ActionChains(self.driver)
                action.move_to_element_with_offset(val, x, y).click().perform()
                print("\nClick al elemento {} coordenada {}, {}".format(selector, x, y))
                t = time.sleep(tiempo)
                return t
        except TimeoutException as ex:
            print(ex.msg)
            print("\nNo se encontro el elemento" + selector)