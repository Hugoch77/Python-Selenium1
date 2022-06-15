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

#Obteniendo todos los links de la web

links = driver.find_elements(By.TAG_NAME, "a")
print("El numero de links que hay en la pagina es: ", len(links))

for num in links:
    print(num.text)

driver.find_element(By.LINK_TEXT, "Date pickers").click()
time.sleep(t)
driver.find_element(By.LINK_TEXT, "JQuery Date Picker").click()
time.sleep(t)

driver.close()