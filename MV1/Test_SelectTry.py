import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")

driver.get("https://demo.seleniumeasy.com/basic-select-dropdown-demo.html")
driver.maximize_window()
t=2

try:
    diasSelect = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//select[@id='select-demo']")))
    dias=Select(diasSelect)
    dias.select_by_visible_text("Sunday")
    time.sleep(t)
    dias.select_by_index(3)
    time.sleep(t)
    dias.select_by_value("Saturday")
except TimeoutException as ex:
    print(ex.msg)

ciudad=Select(driver.find_element(By.ID, "multi-select"))

ciudad.select_by_index(0)
time.sleep(t)
ciudad.select_by_index(2)
time.sleep(t)
ciudad.select_by_index(4)
time.sleep(t)
ciudad.select_by_index(6)

time.sleep(t)
driver.close()