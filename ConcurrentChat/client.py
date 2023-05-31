from socket import *
from threading import *
##############################

HOST = '127.0.0.1'
PORT = 5050
FORMAT = 'utf-8'

client = socket(AF_INET, SOCK_STREAM)
client.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
client.connect((HOST, PORT))

name = input('Enter Your Name: ').encode(FORMAT)
client.send(name)

welcomeMsg = client.recv(1024).decode(FORMAT)
print(welcomeMsg)

def Sending() :
    try:
        while True:
            msg = input('me ::> ').encode(FORMAT)
            client.send(msg)
    except error as e:
        print(e)
        client.close()


def Receiving() :
    try:
        while True:
            msg = client.recv(1024).decode(FORMAT)
            if msg != 'exit':
                print('\n', msg)
            else:
                print('I left Chat')
                client.close()
    except error as e:
        print(e)
        client.close()

sendThread = Thread(target=Sending).start()
receiveThread = Thread(target=Receiving).start()

