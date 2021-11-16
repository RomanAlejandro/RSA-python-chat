import socket
import time
import pickle

HEADER = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1243))
s.listen(5)

clientsocket, address = s.accept()
print(f"Connection from {address} has been established.")

names = [4,8]
data_serial = pickle.dumps(names)
data_len2 = str(len(data_serial))
data2 = bytes(f"{data_len2:<{HEADER}}", 'utf-8')+data_serial
print("LLAVE PUBLICA ENVIADA AL SERVIDOR: ",data2)
clientsocket.send(data2)


data_len = clientsocket.recv(HEADER)
data = b''
data += clientsocket.recv(int(data_len))
data_deserial = pickle.loads(data)
print("LLAVE PUBLICA DEL CLIENTE: ",data_deserial)

