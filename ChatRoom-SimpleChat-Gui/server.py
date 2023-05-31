from socket import *
from tkinter import *
from threading import Thread
###############################
client = None
name = 'Server'

def connectToChat():
    addMessageToChat('Starting Chat....')
    Thread(target=handleClient).start()

def handleClient() :
    global client
    server = socket(AF_INET, SOCK_STREAM)
    server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    server.bind((host.get(), int(port.get())))
    server.listen()
    while True:
        conn, addr = server.accept()
        client = conn
        recieve()

def send():
    msg = sendMessage.get()
    msgToSend = f"{name} : {msg}"
    msgToSend = msgToSend.encode('utf-8')
    client.send(msgToSend)
    addMessageToChat(f"me: {msg}")
    sendMessage.delete(0, END)

#############################GUI####################
window = Tk()
window.title('Chat Room')

####
Label(window, text='Host').pack()
host =  Entry(window)
host.pack(pady=5)
host.insert(0, "127.0.0.1")
####

####
Label(window, text='Port').pack()
port = Entry(window)
port.pack(pady=10)
port.insert(0, '5050')
####

####
Label(window, text='UserName').pack()
username = Entry(window)
username.pack(pady=15)
####

##Connect Button##
connectButton = Button(window, text='Start Chat', command=connectToChat)
connectButton.pack()
#################

## Chat Messages ##
chat = Text(window, height=10)
chat.pack(fill=X)
###################

## send message Entry##
sendMessage = Entry(window)
sendMessage.pack()
#######################

##send Button##
sendButton = Button(window, text='send', command=send)
sendButton.pack()
###############

def addMessageToChat(msg):
    chat.insert(END, '\n')
    chat.insert(END, msg)

def recieve() :
    while True:
        msg = client.recv(4096).decode('utf-8')
        addMessageToChat(msg)

window.mainloop()


