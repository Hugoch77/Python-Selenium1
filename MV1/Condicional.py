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
driver.get("https://demoqa.com/")
driver.maximize_window()

titulo = driver.find_element(By.XPATH, "//img[@src='/images/Toolsqa.jpg']")
print(titulo.is_displayed())

btn = driver.find_element(By.XPATH, "(//div[contains(@class,'card-up')])[1]")

if titulo.is_displayed():
    print("Existe")
    btn.click()
    time.sleep(t)
else:
    print("No existe")

time.sleep(t)
driver.close()