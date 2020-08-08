# -*- coding = utf-8 -*-
# @Time :
# @ Author : Yeeero
# @File : test_class_method.by
# @Software : PyCharm

class Persons:
    def __init__(self, name):
        self.name = name

    @classmethod
    def func(cls):
        print(cls)

    def run(self):
        self.func()

    @staticmethod
    def static_func():
        print("静态方法")


if __name__ == '__main__':
    p = Persons("jack")
    # p.func()
    # Persons.func()
    # p.run()
    Persons.static_func()
    p.static_func()