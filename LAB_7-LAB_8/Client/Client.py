import socket

ClientSocket = socket.socket()
host = '127.0.0.1'
port = 12349

print('Waiting for connection')
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))

Response = ClientSocket.recv(1024)
while True:
    Input = input('File: ')
    ClientSocket.send(str.encode(Input))
    Response = ClientSocket.recv(1024)
    
    if Response.decode('utf-8') != 'No file find:((':
        str_resp = Response.decode('utf-8').split(" ")[1]
        req_file = open('/Users/hamimehrabi/Desktop/PythonLab/Client/'+ Input, "w")
        req_data = req_file.write(str_resp)
        req_file.close()
        
    else:
        print(Response.decode('utf-8'))

ClientSocket.close()