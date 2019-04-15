import socket

TCP_IP="127.0.0.1"
TCP_PORT=5191
BUFFER_SIZE=1024

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((TCP_IP,TCP_PORT))
s.listen(1)
conn,addr=s.accept()
print (('connection address:',addr))
data1 =conn.recv(BUFFER_SIZE).decode()
data2 =conn.recv(BUFFER_SIZE).decode()
data =int(data1)+int(data2)
conn.send((data.encode()))
conn.close()