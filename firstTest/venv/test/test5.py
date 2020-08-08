#-*- coding = utf-8 -*-
#@Time :  
#@ Author : Yeeero
#@File : test5.by
#@Software : PyCharm
import os
import sys
from selenium import webdriver
import time

'''chrome 浏览器 常见问题导致的异常，需要管理员权限运行Chrome，建议使用火狐'''
print(sys.path)
# 获取驱动器路径
driver_path = 'D:/common_soft/chrome/chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)
# driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
time.sleep(2)