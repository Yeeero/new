#-*- coding = utf-8 -*-
#@Time :  
#@ Author : Yeeero
#@File : test2.by
#@Software : PyCharm

from urllib import request
import requests

def main():
    head={
        "referer":"https://www.lagou.com/jobs/list_python?oquery=php%E5%BC%80%E5%8F%91%E5%B7%A5%E7%A8%8B%E5%B8%88&fromSearch=true&labelWords=relative",
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"
    }
    index_url="https://www.lagou.com/jobs/list_python?oquery=php%E5%BC%80%E5%8F%91%E5%B7%A5%E7%A8%8B%E5%B8%88&fromSearch=true&labelWords=relative"
    response = requests.get(index_url,headers=head)
    print(response.text)
    url="https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false"


    data = {
        'first': 'true',
        'pn': 1,
        'kd': 'python'
    }
    resp = requests.post(url,data=data,headers=head)
    print(resp.content.decode('utf-8'))
    print(resp.json())

if __name__ == '__main__':
    main()