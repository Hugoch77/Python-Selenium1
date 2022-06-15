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

t = 0.5
driver = ""
f = ""


@pytest.fixture(scope='module')
def setup_login_uno():
    global driver, f
    driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
    driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
    driver.maximize_window()
    driver.implicitly_wait(20)
    f = FuncionesGlobales(driver)
    f.TextoMixto("id", "Email", "admin@yourstore.com", t)
    f.TextoMixto("id", "Password", "admin", t)
    f.ClickMixto("xpath", "//button[@type='submit'][contains(.,'Log in')]", t)
    print("\nEntrando al sistema login uno")
    yield
    print("Salida del login uno")
    #driver.close()


@pytest.fixture(scope='module')
def setup_login_dos():
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
    yield
    print("Salida del login dos")
    #driver.close()


@pytest.mark.usefixtures("setup_login_uno")
def test_uno():
    print("\nEntrando al sistema uno")
    f = FuncionesGlobales(driver)
    #driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
    f.ClickMixto("xpath", "//a[@href='#'][contains(.,'Customers')]", t)
    f.ClickMixto("xpath", "(//p[contains(.,'Customers')])[2]", t)
    f.TextoMixto("xpath", "//input[contains(@id,'SearchFirstName')]", "Victoria", t)
    f.ClickMixto("xpath", "//button[contains(@id,'search-customers')]", t)
    #Creando un nuevo usuario
    f.ClickMixto("xpath", "//a[@href='/Admin/Customer/Create']", t)
    #f.TextoMixto("xpath", "//input[contains(@id,'Email')]", "Hugo@hpmail.com", t)
    driver.find_element(By.XPATH, "//input[contains(@id,'Email')]").send_keys("Hugo@gm.com" + Keys.TAB + "pass" + Keys.TAB + "Hugo" + Keys.TAB + "Chavez")
    time.sleep(t)
    f.ClickMixto("xpath", "//input[contains(@id,'Gender_Male')]", t)
    driver.find_element(By.XPATH, "//input[contains(@id,'DateOfBirth')]").send_keys("03/27/1997" + Keys.TAB + "Deloitte")
    time.sleep(t)
    f.ClickMixto("xpath", "//input[contains(@id,'IsTaxExempt')]", t)
    f.ClickMixto("xpath", "(//div[contains(@class,'k-multiselect-wrap k-floatwrap')])[1]", t)
    f.ClickMixto("xpath", "//li[@tabindex='-1'][contains(.,'Test store 2')]", t)
    driver.close()


@pytest.mark.usefixtures("setup_login_dos")
def test_dos():
    print("\nEntrando al sistema dos")
    f = FuncionesGlobales(driver)
    f.ClickMixto("xpath", "//b[contains(.,'Admin')]", t)
    f.TextoMixto("id", "searchSystemUser_userName", "David.Morris", t)
    f.ClickMixto("id", "searchBtn", t)
    f.ClickMixto("xpath", "//input[contains(@id,'btnAdd')]", t)
    driver.find_element(By.XPATH, "//input[contains(@id,'systemUser_employeeName_empName')]").send_keys("Hugo Chavez"+Keys.TAB+"Hugoch77"+Keys.TAB+Keys.TAB+"lumberjack77"+Keys.TAB+"lumberjack77")
    time.sleep(t)
    driver.close()
