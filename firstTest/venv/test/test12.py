# -*- coding = utf-8 -*-
# @Time :
# @ Author : Yeeero
# @File : test12.by
# @Software : PyCharm

class A:
    def __init__(self,x):
        self.x = x
    def a1(self,instance):
        return self.x(instance)


class B:
    def b1(self):
        print('b1')

    x = A(b1)
    # x.a1()

b = B()
b.x.a1(b)