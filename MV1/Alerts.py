import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
t=2
driver.get("https://demo.seleniumeasy.com/bootstrap-modal-demo.html")
driver.maximize_window()

driver.find_element(By.XPATH, "//a[@href='#myModal0']").click()
#time.sleep(t)
#driver.find_element(By.XPATH, "(//a[@href='#'][contains(.,'Close')])[1]")
#driver.find_element(By.XPATH, "(//a[@href='#'][contains(.,'Save changes')])[1]").click()
try:
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "(//a[@href='#'])[17]")))
    driver.find_element(By.XPATH, "(//a[@href='#'])[17]").click()
    time.sleep(t)
except TimeoutException as ex:
    print(ex.msg)
    print("El elemento no esta disponible")

time.sleep(t)
driver.close()