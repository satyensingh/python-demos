import socket

host = "" # empty means localhost
port = 5000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
s.sendall("Hello World!")
data = s.recv(1024)
print(data)
s.close()
