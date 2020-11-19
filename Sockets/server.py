import socket
import threading
import time
import secrets

PORT = 5050
# Opcion 1 y 2 para obtener el ip de la pc (el servidor)
SERVER = secrets.SERVER
SERVER = socket.gethostbyname(socket.gethostname())

# Las direcciones deben estar en tuplas para poder enlazarlas al servidor
ADDR = (SERVER, PORT) 

HEADER = 64  # Longitud de cada mensaje
FORMAT = "utf-8"
DISCONECT_MESSAGE = "!DISCONNECT"

# Creo un socket con AF en la familia, INET es ipv4 y el tipo es stream.
# Investigar si hay mas tipos.
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Enlazo el socket a la direccion creada en la tupla
server.bind(ADDR)
connections = []  # Not used


# Esta funcion manejara cada una de las conexiones individuales
def handle_client(conn, addr):
    print("[NEW CONNECTION] {} connected.".format(addr))
    while True:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:  # en conexiones iniciales no entra aqui
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONECT_MESSAGE:
                connections.remove((conn, addr))
                send_to_client("You are disconnected.", conn)
                print("[DISCONNECTION] {} is out.".format(addr))
                print("[ACTIVE CONNECTIONS] {}".format(threading.active_count()-2))
                break
            send_to_client("Msg received.", conn)
            print("[{}] {}".format(addr, msg))          
    conn.close()


def send_to_client(msg:str, conn):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    conn.send(send_length)
    conn.send(message)

# Esta funcion vera que cada conexion sea iniciada en un nuevo 
# hilo del procesador
def start():
    server.listen()
    print("[LISTENING] Server is listening on {}".format(SERVER))
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        # Guardamos la nueva conexion en una lista
        connections.append((conn, addr))
        # Quitamos una en el display porque es el thread de la funcion start
        print("[ACTIVE CONNECTIONS] {}".format(threading.active_count()-1))

print("[STARTING] Server is starting...")

if __name__ == "__main__":
    start()

