# -*- coding = utf-8 -*-
# @Time :
# @ Author : Yeeero
# @File : doutula.by
# @Software : PyCharm
'''利用多线程下载表情包到本地'''
import re
from urllib import parse, request
import os
import threading
from queue import Queue
import requests

tCond = threading.Condition()


class Producter(threading.Thread):
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"}

    def __init__(self, urls_queue, imgs_queue, *args, **kwargs):
        super(Producter, self).__init__(*args, **kwargs)
        self.urls_queue = urls_queue
        self.imgs_quque = imgs_queue

    def run(self):
        while True:
            if self.urls_queue.empty():
                print("以获取全部URL页面，退出生产者模式")
                break
            url = self.urls_queue.get()
            html = self.getPage(url)
            self.parseData(html)

    # 获取页面
    def getPage(self, url):
        resp = requests.get(url, headers=self.head)
        return resp.content.decode('utf-8')

    # 解析页面
    def parseData(self, html):
        # html='''
        # <img referrerpolicy="no-referrer" src="http://img.doutula.com/production/uploads/image/2020/07/18/20200718056632_LOGbWv.jpg"
        # data-original="http://img.doutula.com/production/uploads/image/2020/07/18/20200718056632_LOGbWv.jpg"
        # alt="不玩，不玩我也是你爸爸"
        # class="img-responsive lazy image_dta loaded" data-backup="http://img.doutula.com/production/uploads/image/2020/07/18/20200718056632_LOGbWv.jpg" data-was-processed="true">
        # '''
        re_img = re.compile(r'<img referrerpolicy="no-referrer"\s*src=".*?"\s*data-original="(.+?)"\s*alt="(.+?)".+?>',
                            re.S)
        imgs = re.findall(re_img, html)
        for img_url, alt in imgs:
            alt = re.sub(r'[【】\?？\*，,/！。-]', '', alt)
            file_name = alt + '.' + img_url.split('.')[-1]
            # print(file_name)
            # request.urlretrieve(img_url, 'E:\photos\表情包\\' + file_name)
            # 保存图片到本地
            if not os.path.exists(file_name):
                self.imgs_quque.put((img_url, file_name))
                print(file_name, "已下载完成")


class Consumer(threading.Thread):
    def __init__(self, urls_queue, imgs_queue, *args, **kwargs):
        super(Consumer, self).__init__(*args, **kwargs)
        self.urls_queue = urls_queue
        self.imgs_queue = imgs_queue

    def run(self):
        while True:
            if self.imgs_queue.empty() and self.urls_queue.empty():
                print("图片下载完成，退出")
                break
            img_url, file_name = self.imgs_queue.get()
            request.urlretrieve(img_url, 'E:\photos\表情包\\' + file_name)


def main():
    urls_queue = Queue(100)
    imgs_queue = Queue(1000)
    for p in range(1, 101):
        url = "https://www.doutula.com/photo/list/?page=%s" % str(p)
        urls_queue.put(url)
    for x in range(5):
        t = Producter(urls_queue, imgs_queue)
        t.start()
    for x in range(5):
        t = Consumer(urls_queue, imgs_queue)
        t.start()
    print("saved successfully")


if __name__ == '__main__':
    main()
