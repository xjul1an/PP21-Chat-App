
import socket 
from datetime import datetime
from _thread import start_new_thread
import os


host = '129.217.162.154'
port = 1200

#directory festlegen
directory = os.path.dirname(__file__)

#socket anlegen
sock = socket.socket()
sock.bind((host, port))
sock.listen(1)

#client Liste erstellen
client_list = list()


def start_server():
    while True:
        conn, addr = sock.accept()
        print(addr[0], 'just joined the chat')
        conn.send(b"Welcome to the Server.\n")
        start_new_thread(handle_client, (conn,addr))
        try:
            with open(directory + '/history.txt','r') as text_file:
                history = text_file.read()
        except FileNotFoundError:
            print('The Start of something new...')
            open(directory + '/history.txt','a')
            with open(directory + '/history.txt','r') as text_file:
                history = text_file.read()
        conn.send(history.encode())


def handle_client(conn,addr):
    client_list.append(conn)
    while True:
        #Warten auf Nachrichten der Clientseite
        msg_client_input = conn.recv(1024)
        time_client_input = conn.recv(1024)
        #Ausgabe der Clientnachricht
        print(time_client_input.decode()[:16], addr[0], msg_client_input.decode())
        #An andere Clients senden
        send_to_all_clients(msg_client_input, time_client_input, conn, addr)
        # Chatverlauf speichern
        with open(directory + '/history.txt','a') as text_file:
            text_file.write(time_client_input.decode() + ' ' + addr[0] + ' ' + msg_client_input.decode() + '\n')


def send_to_all_clients(msg_client_input, time_client_input, conn, addr):
    time_client_input += ' '.encode()
    for client in client_list:
        if client == conn:
            continue
        client.send(time_client_input + addr[0].encode() + msg_client_input)


start_server()