# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver=webdriver.Chrome()
# driver.get("https://opensource-demo.orangehrmlive.com/")
# driver.find_element(By.NAME,"username").send_keys("Admin")
# driver.find_element(By.NAME,"password").send_keys("admin123")
#
#
# time.sleep(50)

# assignment 1 # successfully executed
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get("http://admin-demo.nopcommerce.com/login")
driver.find_element(By.NAME,"Email").clear()
driver.find_element(By.NAME,"Email").send_keys("admin@yourstore.com")
driver.find_element(By.ID,"Password").clear()
driver.find_element(By.ID,"Password").send_keys("admin")
driver.find_element(By.XPATH,"/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button").click()
act_title=driver.title
exp_title="Dashboard / nopCommerce administration"
if act_title==exp_title:
    print("Login test passed")
else:
    print("Login test failed")
driver.close()