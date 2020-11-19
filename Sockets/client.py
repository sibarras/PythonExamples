import socket
import secrets  # Esto porque estas importando datos de ahi

HEADER = 64
PORT = 5050
SERVER = secrets.SERVER
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send_to_server(msg:str):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    ans = recieve_from_server()
    print(ans)

def recieve_from_server():
    msg_length = client.recv(HEADER).decode(FORMAT)
    if msg_length:
        msg_length = len(msg_length)
        msg = client.recv(msg_length).decode(FORMAT)
    return msg


msg = input('Manda un mensaje: ')

send_to_server(msg)
input()
send_to_server("Esto es para aprender")
input()
send_to_server("Debes seguir aprendiendo")
input()
send_to_server(DISCONNECT_MESSAGE)