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
driver.get("https://demoqa.com/text-box")
driver.maximize_window()

btn = driver.find_element(By.XPATH, "//button[contains(@id,'submit')]")
print(btn.is_enabled())

if btn.is_displayed():
    print("Puedes dar click")
else:
    print("No puedes dar click")

time.sleep(t)
driver.close()