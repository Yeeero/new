# -*- coding = utf-8 -*-
# @Time :
# @ Author : Yeeero
# @File : test13.by
# @Software : PyCharm

def fibs():
    a = 0
    b = 1
    while True:
        a, b = b, a + b
        yield a


for each in fibs():
    print(each)
    if each > 100:
        break
