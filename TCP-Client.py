import socket
import sys



target_host = sys.argv[1]
target_port = int(sys.argv[2])
target = (target_host,target_port)

#新建socket对象
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#连接客户端
client.connect(target)

#发送数据
client.send(b"GET / HTTP/1.1\r\nHost: 127.0.0.1:10000\r\n")

response = client.recv(4096)
print(response)
