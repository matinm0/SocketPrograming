import socket

PORT = 5050
SERVER = "ip_address of server"
ADDR = (SERVER , PORT)

FORMAT = 'utf-8'
HEADER = 64
DISCONNECT_MESSAGE = "!DISCONNECT"


client = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
client . connect (ADDR)

def send(msg):
    message = msg.encode(FORMAT) 
    msg_len = len(message)
    send_len = str(msg_len).encode(FORMAT)

    send_len += b' '*(HEADER - len(send_len))
    client.send(send_len)
    client.send(message)
  

ready = True
while (ready):
    msg = input("[input a message]  ")
    if msg == 'close':
        ready = False
    send(msg)
    
    


input("Press any key to continue ...")
send(DISCONNECT_MESSAGE)


    
    