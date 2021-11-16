import socket
import pickle

HEADER = 10
####ENVIAR NUESTRA LISTA
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1243))

names = [1,2]
data_serial = pickle.dumps(names)
data_len = str(len(data_serial))
data = bytes(f"{data_len:<{HEADER}}", 'utf-8')+data_serial
print("LLAVE PUBLICA ENVIADA AL SERVIDOR: ",data)
s.send(data)

data_len2 = s.recv(HEADER)
data2 = b''
data2 += s.recv(int(data_len2))
data_deserial = pickle.loads(data2)
print("LLAVE PUBLICA DEL CLIENTE: ",data_deserial)


