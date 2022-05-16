1. 安装python3
    https://www.python.org/downloads/

2. 安装selenium
    pip install selenium
    豆瓣源：
    pip install selenium -i http://pypi.douban.com/simple -- trusted-host pypi.douban.com 

3. 安装webdriver:
    以chrome为例，先查看浏览器版本，chrome://version/
    在http://chromedriver.storage.googleapis.com/index.html找到对应版本的chromedriver
    将chromedriver.exe放到chrome的安装目录下，XXX/Google/Chrome/Application
    将该目录添加到环境变量path中

4. 修改get_cookie.py的第12行、checkin_glados.py的第10行，将路径改为自己需要的

5. 执行get_cookie.py，获取cookie。
    注：该步骤仅需执行一次即可，需要在20s内完成手动登陆。

6. 执行checkin_glados.py

7. 如需自动执行，可以通过windows任务计划程序完成。

8. 如需测试，直接使用python运行脚本即可