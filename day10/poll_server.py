"""
poll_server.py  tcp服务
重点代码

思路： poll() 的返回值不是IO对象
      建立字典 {fileno:io_obj}
"""
from socket import *
from select import *

# 创建监听套接字，作为关注的IO
s = socket()
s.setsockopt(SOL_SOCKET,
             SO_REUSEADDR, 1)
s.bind(('0.0.0.0', 8888))
s.listen(3)

# 创建poll对象
p = poll()

# 建立查找字典
fdmap = {s.fileno(): s}

# 关注s套接字
p.register(s, POLLIN)

# 循环监控IO发生
while True:
    # 提交监控
    events = p.poll()
    print(events)
    for fd, event in events:
        if fd == s.fileno():
            c, addr = s.accept()
            print("Connect from", addr)
            p.register(c, POLLIN | POLLERR)  # 添加新的关注IO
            fdmap[c.fileno()] = c  # 注意维护字典与register保持一致
        elif event & POLLIN:
            # 通过文件描述符取得对象
            data = fdmap[fd].recv(1024).decode()
            print(data)
