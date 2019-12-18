"""

FTP文件服务

一.需求分析

二.技术分析

三.功能模块封装
1.查看内容
2.上传
3.下载

四.协议设置
    请求类型              请求内容
        查看LIST
        上传STOR
        下载DOWNLOAO
            客户端:请求  得到回复
            服务端:
        退出QUIT

五.分模块进行逻辑分析
    网络搭建
        服务端:TCP多线程并发模型
        客户端:链接服务端,打印命令提示界面,通过输入命令决定发送内容
    获取文件类表
"""

"""
fork_server.py   基于fork的多进程服务
重点代码
"""
from socket import *
import os
import signal

# 全局变量
HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST, PORT)


# 处理客户端请求
def handle(c):
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b'OK')
    c.close()

# 创建tcp套接字
s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(ADDR)
s.listen(3)

# 处理僵尸进程产生
signal.signal(signal.SIGCHLD, signal.SIG_IGN)
print("Listen the port 8888...")
while True:
    # 循环接受客户端链接
    try:
        c, addr = s.accept()
        print("Connect from", addr)
    except KeyboardInterrupt:
        s.close()
        os._exit(0)
    except Exception as e:
        print(e)
        continue

    # 客户端链接处理
    pid = os.fork()
    if pid == 0:
        # 处理请求
        s.close()
        handle(c)  # 处理具体请求
        os._exit(0)  # 处理完请求子进程结束
    else:
        c.close()  # 父进程循环回去继续等待其他客户端
