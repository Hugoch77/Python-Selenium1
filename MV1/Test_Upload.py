import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")

driver.get("https://testpages.herokuapp.com/styled/file-upload-test.html")
driver.maximize_window()
t=2

try:
    buscar = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//input[@id='fileinput']")))
    buscar=driver.find_element(By.XPATH, "//input[@id='fileinput']")
    buscar.send_keys("C://Users//Ing. Hugo//PycharmProjects//CursoSelenium//Imagen//demo1.jpg")
    time.sleep(t)
    driver.find_element(By.XPATH, "//input[contains(@id,'itsanimage')]").click()
    time.sleep(t)
    driver.find_element(By.XPATH, "//input[contains(@type,'submit')]").click()
    time.sleep(t)
except TimeoutException as ex:
    print(ex.msg)
    print("Elemento no disponible")

time.sleep(t)
driver.close()