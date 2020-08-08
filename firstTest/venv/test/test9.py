#-*- coding = utf-8 -*-
#@Time :  
#@ Author : Yeeero
#@File : test9.by
#@Software : PyCharm

class Fish():
    def __init__(self):
        pass

    def move(self):
        print('fish')

class Shark(Fish):
    def __init__(self):
        super().__init__()
        self.hungry = True

class CC():
    pass


if __name__ == '__main__':
    print('-'*30)
    sr = Shark()
    sr.move()
    print('-'*30)
    # sr.setXY(4,5)
    print(sr.__dict__)
    print(Shark.__dict__)
    print(Fish.__dict__)
    print(CC)