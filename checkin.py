from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import time
import json
import os

COOKIE = os.environ["COOKIE"]

# 模拟浏览器打开网站
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
browser = webdriver.Chrome('/usr/bin/chromedriver', chrome_options=chrome_options)

browser.get('https://glados.rocks/login')
browser.maximize_window()

for cookie in COOKIE:
    print(cookie)
    browser.add_cookie(cookie)

browser.refresh()

browser.get('https://glados.rocks/console/checkin')
browser.find_element(By.XPATH, "//*[@class='ui positive button']").click()
time.sleep(2)

browser.quit()
