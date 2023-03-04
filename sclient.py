import socket
import random
import string
S = 10 
HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    ran = "The Flag is : " + str(''.join(random.choices(string.ascii_uppercase + string.digits, k = S)))  
    recv_data = ran.encode('ascii')
    s.sendall(recv_data)
    data = s.recv(1024)

print('Received', repr(data))
