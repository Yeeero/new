#-*- coding = utf-8 -*-
#@Time :  
#@ Author : Yeeero
#@File : test7.by
#@Software : PyCharm

'''装饰器'''

def log(func):
    def wrapper():
            print("starting call eat()")
            func()
            print("end eat()")
    return wrapper

def eat():
    print("开始吃了")

# e = log(eat)    # retyrn wrapper
# e()     # wrapper()
log(eat)()