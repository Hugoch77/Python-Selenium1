import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")

driver.get("https://pixabay.com/es/")
driver.maximize_window()
t=2

#driver.execute_script("window.scrollTo(0,1000)")

try:
    buscar = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//label[contains(.,'Descubre más')]")))
    buscar=driver.find_element(By.XPATH, "//label[contains(.,'Descubre más')]")
    ir=driver.execute_script("arguments[0].scrollIntoView();",buscar)
    time.sleep(t)
except TimeoutException as ex:
    print(ex.msg)
    print("Elemento no disponible")

time.sleep(t)
driver.close()