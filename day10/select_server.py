"""

重点代码
    【1】将关注的IO放入对应的监控类别列表
    【2】通过select函数进行监控
    【3】遍历select返回值列表,确定就绪IO事件
    【4】处理发生的IO事件
"""
from select import select
from socket import *

# 创建监听套接字,作为关注的IO
s = socket()
s.setsockopt(SOL_SOCKET,
             SO_REUSEADDR, 1)
s.bind(('0.0.0.0', 8888))
s.listen(3)

# 设置关注的IO
rlist = [s]  # s的 读IO行为
wlist = []  #
xlist = []

while True:
    # 循环监控  s
    rs, ws, xs = select(rlist, wlist, xlist)
    for r in rs:
        if r is s:

            c, addr = rs[0].accept()
            print("Connect from", addr)
            rlist.append(c)
        else:
            data = r.recv(1024).decode()
            if not data:
                # 客户端断开
                rlist.remove(r)  # 不再关注这个IO
                r.close()
                continue
            print(data)
            r.send(b"OK")
