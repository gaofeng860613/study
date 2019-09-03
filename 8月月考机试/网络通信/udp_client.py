from socket import *
ip = '127.0.0.1'
port=8989
address = (ip,port)
buf_size = 1024
udp_client_socket = socket(AF_INET,SOCK_DGRAM)
while 1:
    msg = input('请输入内容:')
    if not msg:
        print('结束发送方程序')
        break
    udp_client_socket.sendto(msg.encode('utf8'), address)
    data1, recv_add = udp_client_socket.recvfrom(buf_size)
    print('服务器返回内容:', data1.decode('utf8'))
udp_client_socket.close()