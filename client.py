import socket 
from _thread import start_new_thread
    
# socket anlegen
host = '127.0.0.1'
port = 5555
sock = socket.socket()
sock.connect((host, port))

def recv_msg():
    while True:
        msg = sock.recv(1024).decode()+'\n'
        print(msg)

start_new_thread(recv_msg, ())

while True: #Sendeschleife
    msg = input().encode()
    sock.send(msg)
