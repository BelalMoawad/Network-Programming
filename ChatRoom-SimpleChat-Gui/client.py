from socket import *
from tkinter import *
from threading import Thread
################################

client = None
name = 'default'

def connectToChat() :
    global client
    global name
    name = username.get()
    client = socket(AF_INET, SOCK_STREAM)
    client.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    client.connect((host.get(), int(port.get())))
    Thread(target=recieve).start()
    chat.insert(END, f"Welcome {name} To Chat")
    client.send(name.encode('utf-8'))

def send() :
    msg = sendMessage.get()
    msgToSend = f"{name} : {msg}"
    msgToSend = msgToSend.encode('utf-8')
    client.send(msgToSend)
    addMessageToChat(f"me: {msg}")
    sendMessage.delete(0, END)

#############################GUI####################
window = Tk()
window.title('Client')

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
connectButton = Button(window, text='Connect', command=connectToChat)
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