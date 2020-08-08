# -*- coding = utf-8 -*-
# @Time :
# @ Author : Yeeero
# @File : test11.by
# @Software : PyCharm

'''  property 函数原理  '''

class MyProperty:
    def __init__(self, fget=None, fset=None, fdel=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel

    def __get__(self, instance, owner):
        print(instance, self.fget)
        return self.fget(instance)

    def __set__(self, instance, value):
        self.fset(instance, value)

    def __delete__(self, instance):
        self.fdel(instance)


class C:
    def __init__(self):
        self._xx = None
        print(self,'-'*20)

    def getX(self):
        return self._xx

    def setX(self, value):
        self._xx = value

    def delX(self):
        del self._xx

    def fun1(self,value):
        print(self)

    x = MyProperty(getX, setX, delX)

c = C()
c.x = 'X-man'
print(c.x)
print(c.getX)
# print(c.fun1(1))