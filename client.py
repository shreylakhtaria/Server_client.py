import socket
#myip.is = to get your public ip addres to join from other pc


HOST = '172.16.101.1'
PORT= 9090


socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((HOST , PORT))

socket.send("hello world!".encode('utf-8'))
print(socket.recv(1024))



