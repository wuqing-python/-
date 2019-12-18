"""
queue_test.py
消息队列演示
"""
from multiprocessing import Queue, Process
from time import sleep
from random import randint

"""
父进程中创建IO，子进程从父进程中获取IO对象，实际上
他们操作的是同一个IO，属性相互影响
如果在各自进程中创建IO对象，那么这些IO对象互相没有
任何影响
"""
# 创建消息队列
q = Queue(3)


def handle():
    while True:
        try:
            # 获取消息
            x, y = q.get(timeout=8)
        except Exception as e:
            print(e)
            break
        else:
            print("%d+%d=%d" % (x, y, x + y))


def request():
    for i in range(6):
        sleep(randint(1, 16))
        x = randint(1, 100)
        y = randint(1, 100)
        q.put((x, y))  # 存入消息


p1 = Process(target=handle)
p2 = Process(target=request)
p1.start()
p2.start()
p1.join()
p2.join()
