import record
from socket import *
import os
from deal_request import *

'''
1.接受请求
2.拿到请求体request
3.处理request
    1.查看路径
    2.查看参数
4返回数据
'''


class Server():
    base_dir = os.path.dirname(__file__)

    def __init__(self, host_port):
        self.head = 'HTTP/1.1 200 OK\r\n\r\n'.encode()
        self.sc = sc = socket()
        sc.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        sc.bind(host_port)
        sc.listen(5)

    def run(self):
        while True:
            print('************************************************************************************************')
            print('listening...')
            self.conn, self.addr = self.sc.accept()
            print('self.conn', self.conn)
            print('self.addr', self.addr)
            request = self.conn.recv(1024).decode()
            print('request', request)
            # 若请求为空，则不处理，继续监听
            if not request:
                self.conn.close()
                continue
            self.handle_request(request)  # 处理请求
            self.conn.close()  # 关闭连接

    # 处理请求
    def handle_request(self, request):
        # 拿到HTTP请求报文的第一行
        first_line = request.splitlines()[0]
        print('first_line', first_line)
        # 去掉第一行末尾的换行符
        first_line = first_line.rstrip('\r\n')
        # 保存请求的方法、路径、版本
        self.req_method, self.req_path, self.req_version = first_line.split()
        print('self.req_method', self.req_method)
        print('self.req_path', self.req_path)
        print('self.req_version', self.req_version)
        self.response(self.req_path, request)

    def response(self, path, request):
        # /127.0.0.1:8000/login
        # username=test&password=123456
        global token_select
        data = request.splitlines()[-1]
        record.record('response', 'path', path)  # 记录
        record.record('response', 'data', data)  # 记录
        if path == '/':
            path = '/index.html'
            self.file_response(path)
        # 登录路径
        elif path.find('/login') != -1:
            token = login(data)
            print('登录！！！！！！！！！！')
            self.conn.sendall(self.head + token.encode())
        # 注册路径
        elif path.find('/register') != -1:
            print('注册！！！！！！！！！')
            return_data = register(data)
            self.conn.sendall(self.head + return_data.encode())
        # 查询路径
        elif path.find('/select') != -1:
            print('查询！！！！！！！！')
            if request.find('accessToken') != -1:
                access_token, token_select = request.splitlines()[6].split(': ')
            data_select = response_select(path, token_select)
            self.conn.sendall(self.head + data_select.encode())
        else:
            self.file_response(path)

    # 针对不同的请求文件，响应不同的请求内容
    def file_response(self, path):
        file_path = self.base_dir + path
        print('file_path:', file_path)
        try:
            with open(file_path, 'rb') as f:
                file = f.read()
            self.conn.sendall(self.head + file)
        except:
            file = 'file wrong'.encode()
            self.conn.sendall(self.head + file)


if __name__ == '__main__':
    server = Server(('127.0.0.1', 8000))
    server.run()
