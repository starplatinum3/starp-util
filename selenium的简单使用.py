# Python爬虫：selenium_蒙小骏的博客-CSDN博客_python爬虫selenium
# https://blog.csdn.net/mengnf/article/details/122876542

import time
from selenium import webdriver

from selenium.webdriver.chrome.options import Options

#  "ChromeOptions" is not definedPylanc
option = ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])
service = Service('data/Application/chromedriver.exe')
driver = Chrome(service=service,options=option)
driver.implicitly_wait(10)
driver.get('https://www.csdn.net/')


#  C:\Users\25004\AppData\Local\Temp\2.46\chromedriver
# 通过指定chromedriver的路径来实例化driver对象，chromedriver放在当前目录。
# driver = webdriver.Chrome(executable_path='./chromedriver')
# chromedriver已经添加环境变量
# D:\proj\springShort\white\White-Jotter\wj-vue\node_modules\_chromedriver@2.46.0@chromedriver\lib\chromedriver\chromedriver.exe
# driver = webdriver.Chrome(executable_path=r'C:\Users\25004\AppData\Local\Temp\2.46\chromedriver')
# driver = webdriver.Chrome()
driver = webdriver.Chrome(executable_path=r'D:\proj\springShort\white\White-Jotter\wj-vue\node_modules\_chromedriver@2.46.0@chromedriver\lib\chromedriver\chromedriver.exe')

# 控制浏览器访问url地址
driver.get("https://www.baidu.com/")
 
# 在百度搜索框中搜索'python'
driver.find_element_by_id('kw').send_keys('python')
# 点击'百度搜索'
driver.find_element_by_id('su').click()
#  ModuleNotFoundError: No module named 'selenium'
# pip install selenium
time.sleep(6)
# 退出浏览器

# D:\software\anaconda\envs\py374\Scripts>pip install selenium
driver.quit()

# pip install selenium
# AttributeError: 'Service' object has no attribute 'process'

# d:\proj\python\my_util_py_pub\selenium的简单使用.py:14: DeprecationWarning: executable_path has been deprecated, please pass in a Service object