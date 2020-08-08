# -*- coding = utf-8 -*-
# @Time :  
# @ Author : Yeeero
# @File : test15.by
# @Software : PyCharm

class Person():
    def __init__(self, name=None, age=None, sex=None):
        self.name = name
        self.age = age
        self.sex = sex

    def __str__(self):
        return "name:{}, age: {}, sex:{}".format(self.name, self.age, self.sex)


class Student(Person):
    def __init__(self, age):
        super(Student, self).__init__()
        self.age = age



if __name__ == '__main__':
    stu = Student(21)
    print(stu)
