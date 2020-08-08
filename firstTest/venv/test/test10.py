#-*- coding = utf-8 -*-
#@Time :  
#@ Author : Yeeero
#@File : test10.by
#@Software : PyCharm

class Person():
    def __getattribute__(self, item):
        print('属性调用')
        return super().__getattribute__(item)

    def __getattr__(self, item):
        print('getattr')
    def __setattr__(self, key, value):
        print('setattr')
        super().__setattr__()
    name = 'YYYY'
    __age=18

p = Person()

print(p.name)
print(p._Person__age)
print(p.x)