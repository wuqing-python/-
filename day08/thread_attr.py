"""
线程对象的属性
"""
from threading import Thread
from time import sleep


def fun():
    sleep(15)
    print("线程对象属性")


t = Thread(target=fun, name='Tarena')

# 主线程退出分支线程也退出
# t.setDaemon(True)

t.start()

t.setName("Tedu")  # 给线程起名字
print("Name:", t.getName())
print("is alive:", t.is_alive())
