from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json

driver = webdriver.Chrome()

driver.get('https://glados.rocks/login')
driver.maximize_window()

with open('D:\Documents\Scripts\glados\cookies.txt','r') as f:
    # read cookies 
    cookies_list = json.load(f)

    for cookie in cookies_list:
        print(cookie)
        driver.add_cookie(cookie)

driver.refresh()

driver.get('https://glados.rocks/console/checkin')
driver.find_element(By.XPATH, "//*[@class='ui positive button']").click()
time.sleep(2)

driver.quit()