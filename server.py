import socket


HOST = '192.168.0.1'
PORT = 9090


#for accepting coonnections or listening
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))



#for communication purpose to connect
server.listen(5)

while True:
    communication_socket, address = server.accept()
    print(f"connected to {address}")
    message = communication_socket.recv(1024).decode('utf-8')
    print(f"Message from client is: {message}")
    communication_socket.send(f"got your message ! thank you!".encode('utf-8'))
    communication_socket.close()
    print(f"connection with {address} ended!")
