import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\Drivers\chromedriver_win32\chromedriver.exe")

driver=webdriver.Chrome(service=serv_obj)
driver.get("https://www.flipkart.com/")
driver.maximize_window()   # maximizes the window
driver.find_element(By.XPATH,"/html/body/div[2]/div/div/button").click()
# sliders=driver.find_elements(By.CLASS_NAME,"_1mIbUg")
# print(len(sliders))   # returns 5..no of slides
links=driver.find_elements(By.TAG_NAME,"a")
print(len(links))    # 345 links found on flipkart
# time.sleep(20)