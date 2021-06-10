import socket
from _thread import start_new_thread
from datetime import datetime

host = '127.0.0.1'
port = 5555
#socket anlegen
sock = socket.socket()
sock.bind((host, port))
sock.listen(1)
print(f"Server({host}) listening on port {port}")

def handle_client(conn, addr):
    while True:
        #Warten auf Nachrichten der Clientseite
        msg = conn.recv(1024)
        # Erfassen der Empfangszeit
        now = datetime.now().strftime("%d.%m.%Y - %H:%M:%S")
        #Ausgabe der Clientnachricht in der Serverkonsole
        print(f"[{addr[0]} at {now}]: {msg.decode()}")


while True: #Serverschleife 
    # Auf neuen Client warten
    conn, addr = sock.accept()
    print(addr[0], ' just joined the chat')
    conn.send(b"Welcome to the Server.\n")
    # Neuen Thread erstellen, der die Client Funktion aufruft.
    start_new_thread(handle_client, (conn, addr))
    
