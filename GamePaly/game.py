class Game:
    def __init__(self):
        self.p1Went = False
        self.p2Went = False
        self.ready = False
        self.moves = [None, None]
        self.wins = [0,0]
        self.ties = 0

    def get_player_move(self, p): # return move of player p
        return self.moves[p]

    def play(self, player, move):
        self.moves[player] = move
        if player == 0:
            self.p1Went = True
        else:
            self.p2Went = True

    def connected(self):
        return self.ready

    def bothWent(self):
        return self.p1Went and self.p2Went

    def winner(self):
        p1 = self.moves[0].upper()[0]
        p2 = self.moves[1].upper()[0]

        if (p1 == "R" and p2 == "S") or (p1 == "P" and p2 == "R") or (p1 == "S" and p2 == "P"):
            return 0
        if (p1 == "S" and p2 == "R") or (p1 == "R" and p2 == "P") or (p1 == "P" and p2 == "S"):
            return 1
        return -1