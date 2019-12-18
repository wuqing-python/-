"""
fork_server.py   基于fork的多进程服务
重点代码
"""
from socket import *
import os

# 全局变量
HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST, PORT)


# 处理客户端请求
def handle(c):
    pass


# 创建tcp套接字
s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(ADDR)
s.listen(3)

print("Listen the port 8888...")
while True:
    # 循环接受客户端链接
    try:
        c, addr = s.accept()
        print("Connect from", addr)
    except KeyboardInterrupt:
        os._exit(0)
    except Exception as e:
        print(e)
        continue

    # 客户端链接处理
    pid = os.fork()
    if pid == 0:
        # 处理请求
        handle(c)  # 处理具体请求
        os._exit(0)
        # 处理完请求子进程结束
    else:
        continue  # 父进程循环回去继续等待其他客户端
