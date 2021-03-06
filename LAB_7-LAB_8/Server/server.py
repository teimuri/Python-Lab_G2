import socket
import os
from _thread import *



import os

def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)
        
        
ServerSocket = socket.socket()
host = '127.0.0.1'
port = 12349
ThreadCount = 0
try:
    ServerSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print('Waitiing for a Connection..')
ServerSocket.listen(5)


def threaded_client(connection):
    connection.send(str.encode('Welcome to the Servern'))
    while True:
        data = connection.recv(2048)
        data_str = data.decode('utf-8')
        
        dum_flag = find(data_str, '/Users/hamimehrabi/Desktop/PythonLab/Server/Storage')
        
        if dum_flag == None:
            reply = 'No file find:(('
            if not data:
                break
            connection.sendall(str.encode(reply))
            
        else:
            req_file = open(dum_flag, "rb")
            req_data = req_file.read()
            req_file.close()
            
            reply = 'data: ' + req_data.decode("utf-8")
            if not data:
                break
            connection.sendall(str.encode(reply))
             
    connection.close()

while True:
    Client, address = ServerSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(threaded_client, (Client, ))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
ServerSocket.close()