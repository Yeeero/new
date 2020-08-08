# -*- coding = utf-8 -*-
# @Time :
# @ Author : Yeeero
# @File : lagou.by
# @Software : PyCharm

from urllib import request, parse
import requests

head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36",
    "Referer": "https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=",
    "authority": "www.lagou.com",
    "origin": "https://www.lagou.com"
}

def main():
    global head
    cookie = getCookie()
    url = "https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false"
    resp = requests.post(url,headers=head,cookies=cookie)
    print(resp.json())

# 获取cookie信息
def getCookie():
    url = "https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput="
    global head
    resp = requests.get(url,headers=head)
    return resp.cookies.get_dict()


if __name__ == '__main__':
    main()
