import socket
import sys


target_host = sys.argv[1]
target_port = int(sys.argv[2])
target = (target_host, target_port)

#新建socket对象
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# #连接客户端
# client.connect(target)

#发送数据
client.sendto(b'10000',target)

data , addr = client.recvfrom(4096)

print(data)
