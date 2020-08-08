# -*- coding = utf-8 -*-
# @Time :
# @ Author : Yeeero
# @File : test1.by
# @Software : PyCharm
import eventlet

import requests
import re
from bs4 import BeautifulSoup
import os
import time


def main():
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"}
    # file_name="E:\photos\壁纸"+"/"+"wallhaven-r2ze21.jpg"
    # if os.path.exists(file_name):
    #     print("exists")
    # else:
    #     print('not exists')

    url = "https://wallhaven.cc/w/r2ze21"
    # print(crawHTML(url))
    with open('ze21.jpg','wb') as f:
        f.write(requests.get("https://w.wallhaven.cc/full/r2/wallhaven-r2ze21.jpg",headers=head).content)
        print("save")


def crawHTML(url):
    head = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"}
    html=requests.get(url, headers=head).content.decode('utf-8')
    # print('hello world')
    return html


# html = crawHTML('https://movie.douban.com/top250')

if __name__ == "__main__":
    main()
