import socket
   
HEADER = 64
TCP_PORT = 5005
FORMAT = 'utf-8' 
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER_TO_CONNECT =  "192.168.137.1"  # This is the ip address of server, not client

ADDR = (SERVER_TO_CONNECT, TCP_PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

send("Hello World")
send("Hello Everyone")
send("Hello Tim")
send(DISCONNECT_MESSAGE)