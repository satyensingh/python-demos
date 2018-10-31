import socket

host = "" # empty means localhost
port = 5000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))
s.listen(1)
connect,address = s.accept() # Here ,(coma) is for Tuples, Read More about tuples
print("client connected from: "+str(address))
while(1):
    data = connect.recv(1024)
    if not data:
        break
    connect.sendall("received: "+ data)
connect.close()





