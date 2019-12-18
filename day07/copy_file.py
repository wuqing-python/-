"""
使用Process创建两个子进程，同时复制
一个文件，分别复制前半部分和后半部分，
形成两个新的文件
"""
from multiprocessing import Process
import os

filename = './bc.jpeg'
size = os.path.getsize(filename)


# fr = open(filename,'rb')

# 复制上半部分
def top():
    fr = open(filename, 'rb')
    fw = open('top.jpg', 'wb')
    n = size // 2
    fw.write(fr.read(n))
    fr.close()
    fw.close()

# 复制下半部分
def bot():
    fr = open(filename, 'rb')
    fw = open('bot.jpg', 'wb')
    fr.seek(size // 2, 0)
    fw.write(fr.read())
    fr.close()
    fw.close()


p1 = Process(target=top)
p2 = Process(target=bot)
p2.start()
p1.start()
p1.join()
p2.join()
