# -*- coding = utf-8 -*-
# @Time :
# @ Author : Yeeero
# @File : xiecheng01.by
# @Software : PyCharm
import time

import greenlet


def task1():
    for i in range(3):
        yield i
        print('------task1----', str(i))
        time.sleep(1)


def task2():
    for i in range(5):
        yield i
        print('----task2', str(i))
        time.sleep(2)


if __name__ == '__main__':
    g1 = task1()
    g2 = task2()

    while True:
        try:
            next(g1)
            next(g2)
        except:
            break