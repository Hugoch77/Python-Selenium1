import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")

driver.get("https://demoqa.com/text-box")
driver.maximize_window()
driver.implicitly_wait(10)

t=.1
time.sleep(t)

nom=driver.find_element(By.XPATH,"//input[contains(@id,'userName')]")
nom.send_keys("Rodrigo")
time.sleep(t)
driver.find_element(By.XPATH,"//input[contains(@id,'userEmail')]").send_keys("Rodrigo@gmail.com")
time.sleep(t)
driver.find_element(By.XPATH,"//textarea[contains(@id,'currentAddress')]").send_keys("Direccion a")
time.sleep(t)
driver.find_element(By.XPATH,"//textarea[contains(@id,'permanentAddress')]").send_keys("Direccion b")
time.sleep(t)
driver.execute_script("window.scrollTo(0,200)")
time.sleep(t)
driver.find_element(By.XPATH,"//button[contains(@id,'submit')]").click()
time.sleep(t)
driver.close()