#-*- coding = utf-8 -*-
#@Time :  
#@ Author : Yeeero
#@File : testmysql.by
#@Software : PyCharm

import pymysql

#1 create connection
conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd='1234',db='test')
#2 create cursor
cur = conn.cursor()
#3 execute sql
#3.1 create a new table
# sql='''
#     create table if not exists student1(
#         id int primary key auto_increment,
#         name varchar(50) not null,
#         age int,
#         gender int default 1,
#         introduction varchar(100)
#     )
# '''
#3.2 insert(add)
# sql="insert into student1(name,age,gender,introduction) values('Keol',18,1,'good good student!')"
#3.3 delete

#3.4 update

#3.5 select
sql = "select * from student1 where age=188"

result = cur.execute(sql)
print(result)
# 将结果集分离出来
data = cur.fetchall()
for d in data:
    print(d)
conn.commit()
cur.close()
conn.close()