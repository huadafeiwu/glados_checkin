from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import json
import os

cookies = os.environ["COOKIE"]

driver = webdriver.Chrome()

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--headless')
browser = webdriver.Chrome(chrome_options=chrome_options)

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
