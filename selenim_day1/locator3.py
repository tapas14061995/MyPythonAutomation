import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://www.facebook.com/")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("tapaschiku")
driver.find_element(By.CSS_SELECTOR,"input[data-testid=royal_pass]").send_keys("Tapas@33")
driver.find_element(By.NAME,"login").click()
time.sleep(20)



