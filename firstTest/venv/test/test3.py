#-*- coding = utf-8 -*-
#@Time :  
#@ Author : Yeeero
#@File : test3.by
#@Software : PyCharm

from lxml import etree
import requests

def main():
    resp = requests.get("http://www.baidu.com")
    # with open('index.html',encoding='utf-8') as f:
    #     f.write(resp.content.decode('utf-8'))
    # html = etree.HTML(resp.text)
    # html = etree.tostring(html)
    # print(etree.tostring(html,encoding='utf-8').decode('utf-8'))
    print(etree.parse(resp.content.decode('utf-8')))

if __name__ == '__main__':
    main()