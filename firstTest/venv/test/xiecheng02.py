# -*- coding = utf-8 -*-
# @Time :
# @ Author : Yeeero
# @File : xiecheng01.by
# @Software : PyCharm
import time
import gevent
from gevent import monkey

monkey.patch_all()


def a():
    for i in range(5):
        print('A------>', str(i))
        time.sleep(0.1)


def b():
    for i in range(5):
        print('B------>', str(i))
        time.sleep(0.2)


def c():
    for i in range(5):
        print('C------>', str(i))
        time.sleep(0.3)


if __name__ == '__main__':
    ga = gevent.spawn(a)
    gb = gevent.spawn(b)
    gc = gevent.spawn(c)

    ga.join()
    gb.join()
    gc.join()