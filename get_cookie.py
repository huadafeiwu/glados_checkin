from selenium import webdriver
import time
import json

driver = webdriver.Chrome()

driver.get('https://glados.rocks/console/checkin')

# 程序打开网页后20秒内手动登陆账户
time.sleep(20)

with open('D:\\Documents\\Scripts\\glados\\cookies.txt','w') as f:
    # save cookies as json
    f.write(json.dumps(driver.get_cookies()))

driver.quit()