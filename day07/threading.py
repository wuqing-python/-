"""
shreading1.py  线程基础使用
"""

import threading
from time import sleep


# 线程函数
def music():
    for i in range(3):
        sleep(2)
        print("哇哦,你的舞跳得真的很不错")


# 创建线程对象
t = threading.Thread(target=music)
t.start()
for i in range(4):
    sleep(2)
    print("难道这就是你分手的借口")

t.join()

