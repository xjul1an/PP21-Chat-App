
import socket 
from datetime import datetime
from _thread import start_new_thread

# socket anlegen
host = '129.217.162.154'
port = 1200
my_address = '129.217.162.154'
sock = socket.socket()
sock.connect((host, port))


def start_client():
    start_new_thread(recieve_data, (host,port))
    while True:
        msg_client_input = input()
        time_client_input = str(datetime.now())[:16]
        sock.send(msg_client_input.encode())
        sock.send(time_client_input.encode())


def recieve_data(host,port):
     while True:
         start_msg = sock.recv(1024).decode()
         print(start_msg)
         history = sock.recv(1024).decode()
         print('History:')
         print(history.replace(my_address, 'Me'))

start_client()

