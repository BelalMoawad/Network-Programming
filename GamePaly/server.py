from socket import *
from threading import Thread
from game import Game
import pickle
#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
clients  = {}
count = 0
game = Game()

def accept_connections():
    global count
    while True:
        con , add = s.accept()
        count += 1
        print(f'{add[1]} has entered game')
        if count == 2:
            game.ready = True
        Thread(target=handleClient ,args=(con, count - 1)).start()  # start thread to handle client

def handleClient(conn, p):
    global count
    clients[conn] = conn
    conn.send(str.encode(str(p)))
    while True:
        try:
            data = conn.recv(BUFF_SIZE).decode()
            if not data:
                break
            else:
                if data != 'get':
                    game.play(p, data)
                print('p1 went: ', game.p1Went)
                print('move1: ', game.moves[0])
                sendToAll() # send changes to all clients
        except:
            break
    conn.close()

def sendToAll():
    for client in clients:
        client.send(pickle.dumps(game))

try:
    s = socket(AF_INET, SOCK_STREAM)
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    HOST = '127.0.0.1'
    PORT = 5555
    s.bind((HOST, PORT))
    s.listen(2)
    print("Waiting for a connection, Server Started")
    BUFF_SIZE = 4096

    t = Thread(target=accept_connections)
    t.start()
    t.join()
    s.close()

    print("exit")
except:
    print("bye")
    exit()