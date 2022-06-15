import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")

driver.get("https://demo.seleniumeasy.com/basic-checkbox-demo.html")
driver.maximize_window()
driver.implicitly_wait(10)
t=2

btn1 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//input[contains(@type,'checkbox')])[1]"))).click()
btn2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//input[contains(@type,'checkbox')])[2]"))).click()
btn3 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//input[contains(@type,'checkbox')])[3]"))).click()

driver.execute_script("window.scrollTo(0,200)")

time.sleep(t)
driver.close()