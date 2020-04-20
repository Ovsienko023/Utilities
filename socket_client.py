import socket


sock = socket.socket()
sock.connect(('localhost', 8888))

sock.send(b'Hello')
data = sock.recv(1024)
print(data)
sock.close()
