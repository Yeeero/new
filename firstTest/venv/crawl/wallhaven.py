# -*- coding = utf-8 -*-
# @Time :
# @ Author : Yeeero
# @File : vmgirls.by
# @Software : PyCharm

import requests
from bs4 import BeautifulSoup
import os
import urllib.request
import re
import time
import eventlet     # 超时跳过

# import sys
# sys.setrecursionlimit(1000000)


# 1 获取目标网页
def main():
    head = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"}
    url = "https://wallhaven.cc/"
    html = drwal(url)
    # print(html)
    f = open("index.html", 'w', encoding='utf-8')
    f.write(html)
    urls = re.findall('<span class="sm-thumb">.*?<a href="(.*?)">', html)
    print(urls)
    # soup = BeautifulSoup(html,"html.parser")
    # for item in soup.find('div',class_="nc-light-gallery").find_all('a', class_="nc-light-gallery-item"):
    count = 0
    for url in urls:
        print(url)
        html2 = drwal(url)
        if html2 == '':
            continue
        src = re.findall('<div class="scrollbox">.*?<img .*? src="(.*?)" .*?>', html2)[0]
        if count >= 100:
            break
        name = src.split('/')[-1]
        print(src, name)
        dir_name = "E:\photos\壁纸"
        if not os.path.exists(dir_name):
            os.mkdir(dir_name)
        # response = requests.get(url, headers=head)
        # 保存图片到电脑
        head = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"}
        if not os.path.exists(dir_name + "/" + name):
            try:
                # 设置超时跳过
                # eventlet.monkey_patch()
                # with eventlet.Timeout(60,False):
                with open(dir_name + "/" + name, "wb") as f:
                    f.write(requests.get(src,headers = head).content)
                    print("saved")
            except Exception as e:
                print(e)


# 爬取指定页面，返回HTML
def drwal(url):
    try:
        head = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"}
        response = requests.get(url, headers=head)
        # print(response.content)
        # req = urllib.request.Request(url, headers=head)
        # response = urllib.request.urlopen(req)
        return response.content.decode('utf-8')
    except Exception as e:
        print(e)
        return ''


if __name__ == "__main__":
    main()
