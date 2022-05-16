from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json
import os

cookies = os.environ["COOKIE"]

driver = webdriver.Chrome()

driver.get('https://glados.rocks/login')
driver.maximize_window()

cookies_list = json.load(cookies)

for cookie in cookies_list:
    driver.add_cookie(cookie)

driver.refresh()

driver.get('https://glados.rocks/console/checkin')
driver.find_element(By.XPATH, "//*[@class='ui positive button']").click()
time.sleep(2)

driver.quit()
