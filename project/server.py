import socket
import threading
import json

# Key constant variable set up
HEADER = 64
PORT = 65432
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

# server initialization
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

# client message receiving function
def recv_msg(conn):
    msg_length = conn.recv(HEADER).decode(FORMAT)

    if msg_length:
        msg_length = int(msg_length)
        msg = conn.recv(msg_length).decode(FORMAT)
        if msg == DISCONNECT_MESSAGE:
            connected = False

        conn.send("Msg recieved".encode(FORMAT))
        return msg

# client handlin function. Handles all requests for client side and send back info from server side storage
def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected")

    connected = True
    while connected:
        msg = recv_msg(conn)

        if msg == "1":
            new_msg = read_collection().encode(FORMAT)
            conn.send(new_msg)

        if msg == "2":
            cardname = recv_msg(conn)
            count = recv_msg(conn)

            newdata = {
                "name":cardname,
                "number":int(count)}
            
            write_collection(newdata)

        if msg == "3":
            card = recv_msg(conn)
            send_info = str(read_card(card)).encode(FORMAT)
            conn.send(send_info)

    conn.close()    

# server start up
def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count()-1}")

# finds card info in json file
def read_card(card):
    with open('card.json') as f:
        data = json.loads(f.read())

        for i in range(len(data["cards"])):
            if data["cards"][i]["name"] == card:
                return data["cards"][i]["number"]

# appends to json file
def write_collection(newdata):
    with open('card.json') as f:
        data = json.loads(f.read())

        data["cards"].append(newdata)

# reads all cards in json file
def read_collection():
    with open('card.json') as f:
        data = json.loads(f.read())

        send_string = ''
        for i in range(len(data["cards"])):
            send_string += f'{i+1}: {data["cards"][i]["name"]}' + '\n'

    return send_string


print("[STARTING] server is starting...")
start()