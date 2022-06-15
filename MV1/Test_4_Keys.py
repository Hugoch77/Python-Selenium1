import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")

t=2

driver.get("https://demoqa.com/text-box")
driver.maximize_window()
time.sleep(5)

nom=driver.find_element(By.CSS_SELECTOR,"#userName")
nom.send_keys("Rodrigo")
nom.send_keys(Keys.TAB + "Rodrigo@gmail.com" + Keys.TAB + "Direccion 1" + Keys.TAB + "Direccion 2" + Keys.TAB + Keys.ENTER)
time.sleep(t)
driver.find_element(By.XPATH, "//span[@class='text'][contains(.,'Check Box')]").click()
time.sleep(t)

driver.get("https://demoqa.com/")
time.sleep(t)

driver.execute_script("window.history.go(-1)")
time.sleep(t)

driver.execute_script("window.history.go(1)")
time.sleep(t)

driver.close()