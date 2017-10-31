import socket
import threading


bind_ip = '0.0.0.0'
bind_port = 10000
bind_data = (bind_ip,bind_port)

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(bind_data)
server.listen(5)
print("正在监听%s:%d"%(bind_ip,bind_port))


def handle_client(client_socket):

    request = client_socket.recv(1024)
    print("[*]Received:%s"%request)


    client_socket.send(b"OK")
    client_socket.close()
while True:
    client,addr = server.accept()
    print("[*]接受来自: %s:%d的连接"%(addr[0],addr[1]))



    client_handler = threading.Thread(target=handle_client,args=(client,))
    client_handler.start()
    