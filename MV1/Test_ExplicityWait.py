import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")

driver.get("https://demo.seleniumeasy.com/")
driver.maximize_window()
driver.implicitly_wait(10)
t=2

btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@href='#'][contains(.,'No, thanks!')]"))).click()
#btn.click()

#driver.find_element(By.XPATH, "//a[@href='#'][contains(.,'No, thanks!')]").click()

time.sleep(t)
driver.close()