# -*- coding = utf-8 -*-
# @Time :
# @ Author : Yeeero
# @File : test6.by
# @Software : PyCharm

# import jieba
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# from pyecharts import Geo
# from wordcloud import WordCloud
import re
import matplotlib
from imageio import imread
import requests

url = "https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false"


def data(page):
    return {
        "first": "true",
        "pn": f"{page}",
        "kd": "python",
        'sid': '4256fece2141497bb5a8e1bfa69bcee7'
    }


def get_cookies():
    headers = {
        'origin': 'https://www.lagou.com',
        'referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
        'authority': 'www.lagou.com',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
    }

    response = requests.get('https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
                            headers=headers)
    return response.cookies.get_dict()


cookies = get_cookies()
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
    , 'host': 'www.lagou.com'
    , 'origin': 'https://www.lagou.com'
    , 'referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='}


def get_data(data):
    response = requests.post(url=url, headers=headers, data=data, cookies=cookies)
    # json数据
    print(response.json())
    content = response.json()['content']['positionResult']['result']
    j = 1
    companyLabelstr = ''
    for i in content:
        city = i['city']
        companyFullName = i['companyFullName']
        companySize = i['companySize']
        education = i['education']
        positionName = i['positionName']
        salary = i['salary']
        workYear = i['workYear']
        companyLabelList = i['companyLabelList']
        if len(companyLabelList) > 0:
            companyLabelList = ''.join(companyLabelList)
        else:
            companyLabelList = ''
        '''
        companyLabelstr=companyLabelList+companyLabelstr
        print(workYear,companyLabelList)
        print(companyLabelstr)
        '''

        with open('python.csv', 'a+', encoding='utf-8')as f:
            f.write(
                f'{city},{companyFullName},{companySize},{education},{positionName},{salary},{workYear},{companyLabelList}\n')

        print(f'第{j}条数据成功')
        j += 1


if __name__ == '__main__':
    for i in range(1, 11):
        params = data(i)
        get_data(params)
        break
