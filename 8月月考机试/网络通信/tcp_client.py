from socket import *
ip = '127.0.0.1'
port=8989
address = (ip,port)
buf_size = 1024
tcp_client_socket = socket(AF_INET,SOCK_STREAM)
tcp_client_socket.connect(address)
while 1:
    msg = input('请输入内容:')
    tcp_client_socket.send(msg.encode('utf8'))
    res1 = tcp_client_socket.recv(buf_size)
    print('服务器返回内容:',res1.decode('utf8'))
tcp_client_socket.close()