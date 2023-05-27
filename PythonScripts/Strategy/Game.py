import Human_Interaction as HI
import Computer_Player as Reachy


class Game:
    def __init__(self):
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.reachy_score = 0
        self.player_score = 0
        self.reachy_moveCounter = 0
        self.player_moveCounter = 0
        self.level = 2

        self.game_closed = False


        # alle möglichen Gewinnkombinationen
        self.wincombinations = [
            [[0,0], [0,1], [0,2]],
            [[1,0], [1,1], [1,2]],
            [[2,0], [2,1], [2,2]],

            [[0,0], [1,0], [2,0]],
            [[0,1], [1,1], [2,1]],
            [[0,2], [1,2], [2,2]],

            [[0,2], [1,1], [2,0]],
            [[0,0], [1,1], [2,2]]
        ]


#berechnet die Summe der Einträge einer Gewinnkombination
    def combovalue(self,k):
        wert = self.board[self.wincombinations[k][0][0]][self.wincombinations[k][0][1]] + self.board[self.wincombinations[k][1][0]][self.wincombinations[k][1][1]] + self.board[self.wincombinations[k][2][0]][self.wincombinations[k][2][1]];
        return wert


    # prüft, ob der neue Spielzustand legal ist
    def check_board(self, input):
        #global board, player_moveCounter
        # max ein neuer Stein
        print(self)
        new_piece = 0
        # alte Steine bleiben unverändert und kein Reachy-stein auf ein leeres Feld
        illegal_change = False
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == 0 and input[i][j] == -1:
                    new_piece += 1
                elif self.board[i][j] != input[i][j]:
                    illegal_change = True
        if new_piece != 1 and illegal_change:
            print("wrong amount of new pieces: " + str(new_piece) + " and illegal change detected")
            return "wrong amount of new pieces: " + str(new_piece) + " and illegal change detected"
        if new_piece != 1:
            print("wrong amount of new pieces: " + str(new_piece))
            return "wrong amount of new pieces: " + str(new_piece)
        if illegal_change:
            print("illegal change detected")
            return "illegal change detected"
        self.board = input
        self.player_moveCounter += 1
        return True


    # prüft, ob jemand gewonnen hat oder es unentschieden ist
    def check_state(self):
        #global game_closed
        #global reachy_score
        #global player_score

        for combo in range(len(self.wincombinations)):
            if self.combovalue(combo) == 3:
                print("Reachy won!")
                self.reachy_score = self.reachy_score + 1
                self.nextLevel(-1)
                self.game_closed = True
            elif self.combovalue(combo) == -3:
                print("Human won!")
                self.player_score = self.player_score + 1
                self.nextLevel(1)
                self.game_closed = True

        found_space = False
        for row in self.board:
            for cell in row:
                if cell == 0:
                    found_space = True
        if not found_space:
            print("No more moves possible...")
            # nextLevel(0)
            self.game_closed = True


    def play(self):
        #global reachy_moveCounter, board
        while not self.game_closed:
            input = HI.make_user_move(self.board)
            if self.check_board(input) == True:
                self.check_state()
                if not self.game_closed:
                    self.board = Reachy.make_computer_move(self.board, self.level, self.reachy_moveCounter, self.player_moveCounter)
                    self.reachy_moveCounter += 1
                    print("reachy moved {} times".format(self.reachy_moveCounter))
                    self.check_state()
                HI.print_board(self.board)
        print("current score: Reachy ({}) : Player ({})".format(self.reachy_score, self.player_score))
        print("You are level", self.level)


    #berechnet nächstes Level, evtl dann auf max Level anpassen
    def nextLevel(self, win_state):
        #global level
        if win_state == -1:
            self.level -= 1
            if self.level == -1:
                self.level = 0
        elif win_state == 1:
            self.level += 1
            if self.level == 3:
                self.level = 2


    def arcadeModus(self):
        # global level
        # global game_closed
        # global board
        # global reachy_moveCounter
        # global player_moveCounter
        h = True
        exit_game = "1"
        while exit_game == "1":
            self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            self.game_closed = False
            self.reachy_moveCounter = 0
            self.player_moveCounter = 0
            first = input("who goes first? \n 1 for Reachy, 2 for Player: ")
            if first == "1":
                # reachy's first move
                self.board = Reachy.make_first_move(self.board,self.reachy_moveCounter)
                self.reachy_moveCounter = self.reachy_moveCounter + 1
                HI.print_board(self.board)
                self.play()
                exit_game = input("Press 1 to play again, Press any button to exit: ")
            elif first == "2":
                HI.print_board(self.board)
                self.play()
                exit_game = input("Press 1 to play again, Press any button to exit: ")
            else:
                print("input invalid")


#arcadeModus()

# board = [[0, -1, 0], [0, 1, 0], [0, 0, 0]]
# input = [[0, -1, 0], [1, 1, 0], [0, -1, 0]]
# print(check_board(input))




