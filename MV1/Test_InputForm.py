import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")

driver.get("https://demo.seleniumeasy.com/input-form-demo.html")
driver.maximize_window()
t=2

try:
    buscar = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//button[contains(.,'Send')]")))

    driver.find_element(By.XPATH, "//input[contains(@name,'first_name')]").send_keys("Hugo" + Keys.TAB + "Chavez" + Keys.TAB + "hhcv@hot.com" + Keys.TAB + "3545411223" + Keys.TAB + "pajapan 5" + Keys.TAB + "Queretaro")
    Estado = Select(driver.find_element(By.XPATH, "//select[contains(@name,'state')]"))
    Estado.select_by_index(5)
    driver.find_element(By.XPATH, "//input[contains(@name,'zip')]").send_keys("80100" + Keys.TAB + "Cardcom.com")
    driver.find_element(By.XPATH, "//input[contains(@value,'no')]").click()
    driver.find_element(By.XPATH, "//textarea[contains(@class,'form-control')]").send_keys("prueba 1 para variar" + Keys.TAB + Keys.ENTER)
    time.sleep(t)

except TimeoutException as ex:
    print(ex.msg)
    print("Elemento no disponible")

time.sleep(t)
driver.close()