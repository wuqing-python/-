"""
http_server2.0
"""


class HTTPServer:
    def __init__(self, host='0.0.0.0', port=80, dir=None):
        self.host = host
        self.port = port
        self.address = (host, port)
        self.dir = dir
        # 直接创建套接字
        self.create_socket()

    # 创建套接子
    def create_socket(self):
        self.sockfd = socket()
        self.sockfd = setsockopt(SOL_SOCKET,SO_REUSEADDR,1)


if __name__ == '__main__':
    # 通过HTTPServer类快速搭建服务
    # 通过该服务让浏览器访问到我的网页
    # 1. 使用流程
    # 2. 需要用户确定的内容

    # 用户决定的参数
    HOST = '0.0.0.0'
    PORT = 8000
    DIR = './static'
    httpd = HTTPServer(HOST, PORT, DIR)  # 生成对象
    httpd.serve_forever()  # 启动服务
