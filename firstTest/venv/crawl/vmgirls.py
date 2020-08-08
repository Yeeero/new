#-*- coding = utf-8 -*-
#@Time :  
#@ Author : Yeeero
#@File : vmgirls.by
#@Software : PyCharm

import requests
from bs4 import BeautifulSoup
import os
import urllib.request
import re
import time

#1 获取目标网页
def main():
    head = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"}
    url = "https://www.vmgirls.com/12945.html/"
    html = drwal(url,head)
    # print(html)
    f = open("index.html",'w',encoding='utf-8')
    f.write(html)
    urls = re.findall('<a href="(.*?)" alt=".*?" title=".*?">', html)
    print(urls)
    # soup = BeautifulSoup(html,"html.parser")
    # for item in soup.find('div',class_="nc-light-gallery").find_all('a', class_="nc-light-gallery-item"):
    for url in urls:
        time.sleep(1)
        title = "你与晚霞同样浪漫"
        name=url.split('/')[-1]
        print(url, name)
        dir_name="E:\photos\唯美女孩"+"/"+title
        if not os.path.exists(dir_name):
            os.mkdir(dir_name)
        response = requests.get(url,headers=head)
        # 保存图片到电脑
        with open(dir_name+"/"+name,"wb") as f:
            f.write(response.content)
            print("saved")
    print(title + "已全部下载完成")

# 爬取指定页面，返回HTML
def drwal(url,head):
    response = requests.get(url, headers = head)
    # print(response.content)
    # req = urllib.request.Request(url, headers=head)
    # response = urllib.request.urlopen(req)
    return response.content.decode('utf-8')

if __name__ == "__main__":
    main()