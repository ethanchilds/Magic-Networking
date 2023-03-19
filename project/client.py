import socket

# Key constant variable set up
HEADER = 64
PORT = 65432
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

# client initialization
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

# Function that will send messages to the server and return a confirmation message
def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

# allows user to send choose some interaction with the server
print("""What would you like to do?
    1. Print cards in collection
    2. Add card to collection
    3. Get card info
(Please respond with a 1,2 or 3)
""")
choice_msg = str(input())
send(choice_msg)

# handles message retreival for option 1
if choice_msg == "1":
    print(client.recv(2048).decode(FORMAT))

# handles message sending and retreival for option 2
if choice_msg == "2":
    cardname = str(input("What is the card name? "))
    send(cardname)

    count = str(input("How many of this card do you have? "))
    send(count)

# handles message sending and retreival for option 3
if choice_msg == "3":
    card = str(input("What is the card name? "))
    send(card)

    print(client.recv(2048).decode(FORMAT))