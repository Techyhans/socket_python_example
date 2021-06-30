import socket
import threading

# To enable communication between server and client via ethernet cable connection:

# (If you are using device with window os as server) we need to go to control panel -> Network and Internet -> Network and Sharing Center
# When server and client devices are connected with an ethernet cable, a network (unidentified network) other than private network will pop up.
# Click the Wi-Fi icon -> Properties -> Sharing -> Tick Allow other network user to connect through this computer's internet connection 
# Then click the Ethernet icon -> Properties -> Networking -> Double click (TCP/IPv4) -> Tick use the following ip address -> Take note of the ip address
# The ip address will be the server ip address

# (If you are using device with linux os as server) we need to open terminal and type ifconfig, 
# Then we look at the eth0 -> inet, if the ethernet cable is connected between two devices, an ip address should be shown up.
# The ip address will be the server ip address

TCP_IP = '192.168.137.1'  # This is the ip address of the server
#TCP_IP = socket.gethostbyname(socket.gethostname())
TCP_PORT = 5005

HEADER = 64
FORMAT = 'utf-8' 
DISCONNECT_MESSAGE = "!DISCONNECT"


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((TCP_IP, TCP_PORT))


def handle_client(conn, addr):
    print (f"[NEW CONNECTION] {addr} connected.")
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            print(f"[{addr}] {msg}")
            conn.send("Msg received".encode(FORMAT))
    conn.close()

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {TCP_IP}")
    while True:
        conn, addr = server.accept() 
        thread = threading.Thread(target= handle_client, args = (conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTION] {threading.activeCount() - 1}")



print("[SERVER] sever is starting ...")
start()