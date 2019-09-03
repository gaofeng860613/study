from socket import *
ip = '127.0.0.1'
port=8989
address = (ip,port)
buf_size = 1024
udp_server_socket = socket(AF_INET,SOCK_DGRAM)
udp_server_socket.bind(address)
while 1:
    data1, send_add = udp_server_socket.recvfrom(buf_size)
    print('接收客户端内容:',data1.decode('utf8'))
    msg = input('请输入还会内容:')
    udp_server_socket.sendto(msg.encode('utf8'), send_add)
udp_server_socket.close()