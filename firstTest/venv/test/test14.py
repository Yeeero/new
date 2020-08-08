#-*- coding = utf-8 -*-
#@Time :  
#@ Author : Yeeero
#@File : test14.by
#@Software : PyCharm

import requests
from lxml import etree


def main():
    url="https://www.qiushibaike.com/text/page/1"
    text = crawl(url)
    # parser = etree.HTMLParser(encoding='utf-8')
    # html = etree.parse(text, parser=parser)
    html = etree.HTML(text)
    stories = html.xpath("//div[@class='content']")
    for story in stories:
        print('-'*30)
        print(story)
        break


def crawl(url):
    resp = requests.get(url)
    return resp.text


if __name__ == '__main__':
    main()