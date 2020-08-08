# -*- coding = utf-8 -*-
# @Time :
# @ Author : Yeeero
# @File : test8.by
# @Software : PyCharm

def log():
    def talk():
        print('talk')

    return talk


def eat():
    print('eat')

print(eat)
eat = log()
eat()
print(log,eat)