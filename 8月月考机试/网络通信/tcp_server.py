from socket import *
ip = '127.0.0.1'
port=8989
address = (ip,port)
buf_size = 1024
tcp_server_socket = socket(AF_INET,SOCK_STREAM)
tcp_server_socket.bind(address)
tcp_server_socket.listen(10)
con,c_add = tcp_server_socket.accept()
while 1:
    data1 = con.recv(buf_size).decode('utf8')
    print('接收客户端内容:',data1)
    msg = input('请输入还会内容:')
    con.send(msg.encode('utf8'))
con.close()