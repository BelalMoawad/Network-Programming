from socket import *
from threading import *
###########################

HOST = '127.0.0.1'
PORT = 5050
FORMAT = 'utf-8'

clients = {}

def acceptConnections() :
    while True:
        conn, addr = server.accept()
        print(f"{addr[1]} entered chat room")
        Thread(target=handleClient, args=[conn,]).start()


def handleClient(conn) :
    name = conn.recv(1024).decode(FORMAT)
    print(name)
    msg = "welcome " + name + " write exit to quit Chat"
    msg = msg.encode(FORMAT)
    conn.send(msg)
    clients[conn] = conn
    sendToAll("{} has entered chat".format(name), "", conn)
    left = f"{name} : has left chat"
    try:
        while True:
            msg = conn.recv(1024).decode(FORMAT)
            print(f"{name} : {msg}")
            if msg != 'exit' :
                sendToAll(msg, name, conn)
            else :
                conn.send(msg.encode(FORMAT))
                del clients[conn]
                sendToAll(left, "", None)
                conn.close()
    except:
        sendToAll(left, "", None)



def sendToAll(msg, sender, conn1) :
    newMSG = sender+"::"+msg
    msg = newMSG.encode(FORMAT)
    for client in clients :
        if client != conn1:
            client.send(msg)


try:
    server = socket(AF_INET, SOCK_STREAM)
    server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen(10)
    print('Starting server...')
    t = Thread(target=acceptConnections)
    t.start()
    t.join()
    server.close()
    print('Closing Server')
except:
    print('bye')
    exit()
