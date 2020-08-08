#-*- coding = utf-8 -*-
#@Time :  
#@ Author : Yeeero
#@File : test4.by
#@Software : PyCharm
import threading
import time
import random
'''生产者与消费者模式'''

gmoney=1000
glock = threading.Lock()
product_times = 10
bankrupt_times = 0

class Producter(threading.Thread):
    def run(self):
        global gmoney
        global product_times
        while product_times:
            money = random.randint(100,1000)
            glock.acquire()
            gmoney += money
            product_times -= 1
            print("%s线程生产了%d￥，总资产%d￥"%(threading.current_thread(),money,gmoney))
            glock.release()
            time.sleep(0.5)

class Consumer(threading.Thread):
    def run(self):
        global gmoney
        global bankrupt_times
        while bankrupt_times <= 10:
            money=random.randint(100,1000)
            glock.acquire()
            if gmoney >= money:
                gmoney -= money
                print("%s线程消费了%d￥，总资产%d￥" % (threading.current_thread(), money, gmoney))
            else:
                bankrupt_times += 1
                print("%s线程资金不足，总资产%d￥" % (threading.current_thread(), gmoney))
            glock.release()
            time.sleep(0.5)

if __name__ == '__main__':
    for x in range(5):
        t = Producter(name="生产者线程%d"%x)
        t.start()
    for x in range(3):
        t = Consumer(name="消费者线程%d"%x)
        t.start()