import socket


PORT = 5050
SERVER = socket.gethostbyname (socket.gethostname())
ADDR = (SERVER , PORT)

HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client( conn , addr ):
    print(f"[NEW CONNECTION] {addr} connected.")
    
    connected = True
    while connected :
      
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length :
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                    connected = False
                    server.close()
            
            print(f"[{addr}] {msg}")
            conn.send(f"[RECIEVED] {addr} ")
            
            
    conn.close()
    
def start():
    server.listen()
    print(f"[LISTENING] server is listening on ip : {SERVER}")
    while True:
        conn , addr = server.accept()
        handle_client(conn , addr)
        print(f"[ACTIVE CONNECTION] {addr}")

        
        
        
print("[STARTING] server is starting ...")
start()

