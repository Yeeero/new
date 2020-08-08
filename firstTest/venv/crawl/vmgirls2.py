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
import pymysql

'''
    功能介绍：获取唯美女孩所有图片的src并保存到数据库
'''


def main():
    # 唯美女孩网站
    url = "https://www.vmgirls.com/"
    # 初始页面（首页）的获取
    html1 = drwalHTML(url)
    f = open("index.html", 'w', encoding='utf-8')
    f.write(html1)
    # print(html)
    # 获取所有主题的链接地址
    # urls = re.findall('<a href="(.*?)" class=".*?" style=.*?>', html1)
    soup = BeautifulSoup(html1,'html.parser')
    count = 0
    urls = []
    for a in soup.find_all('a',class_="media-content"):
        data = []
        try:
            url = a.attrs['href']
            title = a.attrs['title']
            data.append(url)
            data.append(title)
            urls.append(data)
            # print(url,count)
            count += 1
            if count >= 40:
                break
        except Exception as e:
            print(e)

    print(urls)
    # 保存图片
    themeHTML(urls)


# 爬取指定页面，返回HTML
def drwalHTML(url):
    # 伪装浏览器 headers
    head = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"}
    response = requests.get(url, headers=head)
    return response.content.decode('utf-8')


# 保存图片
def themeHTML(urls):
    for data in urls:
        url = data[0]
        title = data[1]
        # 判断该主题是否已保存
        sql = "select * from vmgirls where url='%s'" % url
        if executeSQL(sql) == 0:
            # 遍历获取指定主题HTML
            html2 = drwalHTML(url)
            # 获取主题所有图片的srcs
            srcs = re.findall('<a href="(.*?)" alt=".*?" title=".*?">', html2)
            # 获取主题
            # titles = re.findall('<h1 class="post-title h3">(.*?)</h1>')[0]
            # 获取每张图片的src，并保存到数据库
            for src in srcs:
                pic_name = src.split('/')[-1]
                print(url, pic_name)
                # 保存图片到数据库
                sql = 'insert into vmgirls(url,pic_name,src,title) values("%s","%s","%s","%s")' % (url, pic_name, src, title)
                print(executeSQL(sql))


# execute sql
def executeSQL(sql):
    # 创建数据库连接
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='1234', db='test')
    # create cursor
    cur = conn.cursor()
    # execute
    result = cur.execute(sql)
    conn.commit()
    cur.close()
    conn.close()
    return result


if __name__ == "__main__":
    main()
