#-*- coding = utf-8 -*-
#@Time :  
#@ Author : Yeeero
#@File : vmgirls3.by
#@Software : PyCharm

import pymysql
import os
import requests

def main():
    # 从数据库获取数据
    datas = getdata()
    # download pic to computer
    dir_name = "E:\photos\唯美女孩"
    for data in datas:
        if not os.path.exists(dir_name+'/'+data[0]):
            os.mkdir(dir_name+'/'+data[0])
        # save to computer
        head = { "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"}
        with open(dir_name+'/'+data[0]+'/'+data[1],'wb') as f:
            f.write(requests.get(data[2],headers = head).content)

def getdata(title=''):
    conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd='1234',db='test')
    cur = conn.cursor()
    sql = 'select title,pic_name,src from vmgirls'
    if title:
        where = " where title='%s'"%title
        sql += where
        print(sql)
    cur.execute(sql)
    datas = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    return datas

if __name__ == '__main__':
    main()