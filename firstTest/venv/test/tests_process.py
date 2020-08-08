# -*- coding = utf-8 -*-
# @Time :
# @ Author : Yeeero
# @File : tests_process.by
# @Software : PyCharm

from multiprocessing import Process
import time
import os


def task1():
    while True:
        time.sleep(1)
        print("--------这是task1------", os.getpid(), '-------', os.getppid())


def task2():
    while True:
        time.sleep(1)
        print("--------这是task2------")


if __name__ == '__main__':
    p1 = Process(target=task1, name='processing---1')
    p2 = Process(target=task2, name='processing---2')
    p1.start()
    p2.start()