#-*- coding = utf-8 -*-
#@Time :  
#@ Author : Yeeero
#@File : weather.by
#@Software : PyCharm

from lxml import etree
from bs4 import BeautifulSoup
import requests
from pyecharts import Bar

def main():

    url="http://www.weather.com.cn/textFC/hb.shtml"
    html = crawlPata(url)
    # print(html)
    #2 parse data
    data = []
    data = parsedata(html)
    print(data)
    # sort data
    # data.sort(key=lambda x:x[1],reverse=False)
    data.sort(key=lambda x:x['min_tem'],reverse=False)
    print(data)

# crawl page
def crawlPata(url):
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"}
    resp = requests.get(url,headers=head)
    return resp.content.decode('utf-8')


def parsedata(html):
    data=[]
    elementHtml = etree.HTML(html)
    parser = etree.HTMLParser(encoding='utf-8')
    # html=etree.parse(html,parser=parser)
    tbs = elementHtml.xpath("//table")
    for tb in tbs:
        trs=tb.xpath('.//tr')
        for index,tr in enumerate(trs[2:]):
            dic={}
            # print('='*30)
            tds = tr.xpath(".//td")
            if index == 0:
                pro = tds[1].xpath(".//a/text()")[0]
                min_tem = tds[-2].xpath(".//text()")[0]
            else:
                pro = tds[0].xpath(".//a/text()")[0]
                min_tem = tds[-2].xpath(".//text()")[0]
            dic['area'] = pro
            dic['min_tem'] = int(min_tem)
            data.append(dic)
            # print(pro,int(top_tem))
        # print('-'*30)
    return data

if __name__ == '__main__':
    main()