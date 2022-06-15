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
driver.get("https://demo.seleniumeasy.com/input-form-demo.html")
driver.maximize_window()

btn = driver.find_element(By.XPATH, "//button[contains(@class,'btn btn-default')]")
btn.click()
time.sleep(t)
name_val = driver.find_element(By.XPATH, "//small[@class='help-block'][contains(.,'Please supply your first name')]")
name = name_val.text
print("El valor del error es: ", name)

if name == "Please supply your first name":
    print("Falta el nombre")
    driver.find_element(By.XPATH, "//input[contains(@name,'first_name')]").send_keys("Hugo")
else:
    print("Nombre correcto")

print(btn.is_enabled())
if btn.is_enabled() == False:
    print("Faltan campos por llenar")
else:
    print("Todo listo")

time.sleep(t)
driver.close()