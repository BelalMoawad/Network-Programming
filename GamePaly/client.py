from socket import *
from tkinter import *
import pickle
import time
#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\

client = socket(AF_INET, SOCK_STREAM)
client.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

HOST = '127.0.0.1'
PORT = 5555
ADDR = (HOST, PORT)
BUFF_SIZE = 4096

def connect():
    client.connect(ADDR)
    return client.recv(BUFF_SIZE).decode()

def send(data):
    try:
        client.send(str.encode(data))
        return pickle.loads(client.recv(BUFF_SIZE))
    except error as e:
        str(e)

def redrawWindow(game, p,root):

    if not (game.connected()):
        label = Label(root, text="Waiting for Player...", fg='black')
        label.pack()
        root.update()
    else:
        Label(root, text='Your Move', fg='orange').place(x=80, y=200)
        Label(root, text='Opponents', fg='orange').place(x=380, y=200)

        move1 = game.get_player_move(0)
        move2 = game.get_player_move(1)
        text1 = Label(root, text='', fg='black')
        text2 = Label(root, text='', fg='black')
        if game.bothWent():
            text1['text'] = move1
            text2['text'] = move2
        else:
            if game.p1Went and p == 0:
                text1['text'] = move1
            elif game.p1Went:
                text1['text'] = 'Locked In'
            else:
                text1['text'] = 'Waiting...'

            if game.p2Went and p == 1:
                text2['text'] = move2
            elif game.p2Went:
                text2['text'] = 'Locked In'
            else:
                text2['text'] = 'Waiting...'

        if p == 1:
            text2.place(x=100, y=350)
            text1.place(x=400, y=350)
            root.update()
        else:
            text1.place(x=100, y=350)
            text2.place(x=400, y=350)
            root.update()




def main():
    player = int(connect())
    print("You are player: ", player)
    while True:
        root = Tk()
        root.title('Client')
        root.geometry('600x600')
        try:
            game = send('get')
        except:
            print("Couldn't get game")
            break

        def handleR():
            game = send('Rock')
            redrawWindow(game, player, root)
            root.update()

        def handleS():
            game = send('Scissors')
            redrawWindow(game, player, root)
            root.update()

        def handleP():
            game = send('Paper')
            redrawWindow(game, player, root)
            root.update()

        Button(root, text='Rock', fg='white', bg='red', activebackground='yellow', command=handleR).pack()
        Button(root, text='Scissors', fg='white', bg='green', activebackground='yellow', command=handleS).pack()
        Button(root, text='Paper', fg='white', bg='blue', activebackground='yellow', command=handleP).pack()

        if game.bothWent():
            redrawWindow(game, player, root)
            root.update()

            if game.winner() == player:
                text = Label(text='You Won!', fg='purple')
            elif game.winner() == -1:
                text = Label(text='Tie Game!', fg='purple')
            else:
                text = Label(text='You Lost...', fg='purple')

            text.pack(padx=100, pady=20)
            root.update()

        redrawWindow(game, player, root)
        root.mainloop()



main()
