"""
自定义线程类
"""
from threading import Thread
from time import sleep, ctime


class MyThread(Thread):
    def __init__(self):
        super().__init__()  # 此行不许动


# ===========================================
def player(sec, song):
    for i in range(3):
        print("Playing %s:%s" % (song, ctime()))
        sleep(sec)

t = MyThread(target=player,args=(2),
             kwargs={'song': '凉凉'})
t.start()
t.join()
