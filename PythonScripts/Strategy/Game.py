import random
from . import Human_Interaction as HI
from . import Computer_Player as Reachy
from Movement.MoveFacade import MoveFacade 
from Perception.PerceptionFacade import PerceptionFacade
import time
from Movement.Enums.Animation import Animation
from Movement.Enums.Sentence import Sentence

class Game:
    def __init__(self):
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.reachy_score = 0
        self.player_score = 0
        self.reachy_moveCounter = 0
        self.player_moveCounter = 0
        self.level = 1
        self.enableCheating = True
        self.winHistory = []

        self.game_closed = False

        self.thinkProbability = {
            0: 0,
            1: 20,
            2: 40,
            3: 60
        }


        self.first = 0 #Startspieler (1 = reachy / 2 = player)

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
    
    def set_dependency(self, move : MoveFacade, perc : PerceptionFacade):
        self.move = move
        self.perc = perc


#berechnet die Summe der Einträge einer Gewinnkombination
    def combovalue(self,k):
        wert = self.board[self.wincombinations[k][0][0]][self.wincombinations[k][0][1]] + self.board[self.wincombinations[k][1][0]][self.wincombinations[k][1][1]] + self.board[self.wincombinations[k][2][0]][self.wincombinations[k][2][1]];
        return wert


    # prüft, ob der neue Spielzustand legal ist
    def check_board(self, input):
        # max ein neuer Stein
        new_piece = 0
        # alte Steine bleiben unverändert und kein Reachy-stein auf ein leeres Feld
        illegal_change = False
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == 0 and input[i][j] == -1:
                    new_piece += 1
                elif self.board[i][j] != input[i][j]:
                    illegal_change = True
        if new_piece == 3:
            if random.random() < 0.4:
                print("Damn, 3 game figures at once?!?")
                self.move.do_animation(Animation.ANGRY)
                self.game_closed = True
                return False
        if new_piece != 1 and illegal_change:
            print("wrong amount of new pieces: " + str(new_piece) + " and illegal change detected")
            self.move.do_say(Sentence.ILLEGALMOVE_HM)
            return False
        if new_piece != 1:
            print("wrong amount of new pieces: " + str(new_piece))
            return False
        if illegal_change:
            print("illegal change detected")
            self.move.do_say(Sentence.ILLEGALMOVE_HM)
            return False
        # check if reachys chance was ruined
        self.check_win_rui(input)
        self.board = input
        self.player_moveCounter += 1
        return True


    # prüft, ob jemand gewonnen hat oder es unentschieden ist
    def check_state(self, move: MoveFacade):
        for combo in range(len(self.wincombinations)):
            if self.combovalue(combo) == 3:
                #move.do_animation(Animation.WIN)
                print("Reachy won!")
                self.reachy_score = self.reachy_score + 1
                self.nextLevel(-1)
                self.game_closed = True
                self.react(1, self.move)
            elif self.combovalue(combo) == -3:
                #move.do_animation(Animation.LOOSE)
                print("Human won!")
                self.player_score = self.player_score + 1
                self.nextLevel(1)
                self.game_closed = True
                self.react(-1, self.move)

        if self.player_moveCounter + self.reachy_moveCounter == 9 and not self.game_closed:
            print("No more moves possible...")
            self.game_closed = True
            self.react(0, self.move)
        elif not self.game_closed and self.regtie():
                print("incoming Tie")
                move.do_say(Sentence.DETECT_TIE)
        if self.enableCheating:
            Reachy.scan_trap(self.board, move)

    def react(self, last, move: MoveFacade):
        self.winHistory.append(last)
        history = sum(self.winHistory[-3:])
        # falls 3x nicht gewonnen, letztes verloren: angry
        if last == -1 and history <= -1:
            #print('Reachy is angry')
            move.do_animation(Animation.ANGRY)
        elif last == -1:
            #print('Reachy is sad')
            move.do_animation(Animation.LOSE)
        # falls zwei mal verloren, danach gewonnen: super happy
        if last == 1 and history == -1:
            #print('Reachy does the arm-dance')
            move.do_animation(Animation.WIN)
        elif last == 1:
            #print('Reachy has happy antennaes')
            move.do_animation(Animation.HAPPY)
        # falls 3x unentschieden in Level 3: frustriert
        if self.winHistory.count(0) == 3 and self.level == 3:
            print('Reachy wants to leave')
            move.do_say(Sentence.JOKE)



    def check_combo_move(self, n):
        for combo in range(len(self.wincombinations)):
            if self.board[self.wincombinations[combo][0][0]][self.wincombinations[combo][0][1]] + self.board[self.wincombinations[combo][1][0]][self.wincombinations[combo][1][1]] + self.board[self.wincombinations[combo][2][0]][self.wincombinations[combo][2][1]] == n:
                
                for i in range(3):
                    if self.board[self.wincombinations[combo][i][0]][self.wincombinations[combo][i][1]] == 0:
                        return True
        return False
    
    def think(self):
        p = random.randint(0, 100)
        if p < (100 - self.thinkProbability[self.level]):
            return False
        self.move.do_animation(Animation.CLUELESS)

    #Unentschieden frühzeitig erkennen
    def regtie(self):
        #print("regtie aufgerufen")
        moves = self.reachy_moveCounter + self.player_moveCounter
        chanceReachy = self.check_combo_move(2)
        chancePlayer = self.check_combo_move(-2)
        chances = chanceReachy or chancePlayer
        #print("chances=",chances)
        if self.first == 1 and moves == 8:
            if not chanceReachy: return True

        #wenn keine Gewinnchancen in 1Zug vorliegen
        if not chances:
            if moves == 7: return True
            #liegen auch keine Gewinnchancen in 2 vor, (da 1.Fall: Felder isoliert o. 2.Fall: jeder 1Feld davon) wenn es 2 freie Felder gibt)
            if moves == 6:
                #(oder da GKs max 1 gemeinsames Feld besitzen wenn es eine leere GK gibt)
                for combo in range(len(self.wincombinations)):
                    if (combo == 1 or 4 or 6 or 7) and self.combovalue(combo) == 0:
                        #print("tie erkannt in regtie")
                        self.move.do_animation(Animation.TIE)
                        return True
        #print("kein tie erkannt in regtie")
        return False
    

    def check_win_rui(self, inputBoard):
        #inputBoard ist das neue Board
        #wo konnte Reachy vorher gewinnen? wird in Array gespeichert, Summe muss 2 sein
        möglicheGewinne = []
        for k in range(len(self.wincombinations)):
            wert = self.board[self.wincombinations[k][0][0]][self.wincombinations[k][0][1]] + self.board[self.wincombinations[k][1][0]][self.wincombinations[k][1][1]] + self.board[self.wincombinations[k][2][0]][self.wincombinations[k][2][1]];
            if wert == 2:
                möglicheGewinne += [k]
        print('möglicheGewinne: ', möglicheGewinne)
        #überprüfen ob Gewinn verhindert wurde, dann muss Summe von vorheriger GewinnCombi nun 1 sein
        if len(möglicheGewinne) == 1:
            for i in möglicheGewinne:
                wertNeu = inputBoard[self.wincombinations[i][0][0]][self.wincombinations[i][0][1]] + inputBoard[self.wincombinations[i][1][0]][self.wincombinations[i][1][1]] + inputBoard[self.wincombinations[i][2][0]][self.wincombinations[i][2][1]];
                if wertNeu == 1:
                    print("Reachys Gewinn wurde ruiniert!")
                    # Audio für Spieler verhindert Sieg einfügen
                    return True
        #es wurde kein Gewinn verhindert
        return False


    def play(self, move: MoveFacade):
        while not self.game_closed:
            counter = 0
            check_board_status = False
            move.do_say(Sentence.NEXT_MOVE_HM)
            while counter <= 4:
                time.sleep(3)
                input = HI.make_user_move_unity(self.board, self.perc)
                #input = HI.make_user_move(self.board)
                counter = counter + 1
                check_board_status = self.check_board(input)
                if check_board_status == True:
                    self.check_state(self.move)
                    if not self.game_closed:
                        move.do_say(Sentence.NEXT_MOVE_RH)
                        self.think()
                        self.board = Reachy.make_computer_move(self.board, self.level, self.reachy_moveCounter, self.player_moveCounter, self.move)
                        self.reachy_moveCounter += 1
                        print("reachy moved {} times".format(self.reachy_moveCounter))
                        self.check_state(self.move)
                    HI.print_board(self.board)
                    counter = 5
                move.do_animation(Animation.CLUELESS)
            if check_board_status == False:
                move.do_animation(Animation.DISAPPROVAL)
                # print("reachy shakes head")
                continue
        print("current score: Reachy ({}) : Player ({})".format(self.reachy_score, self.player_score))
        print("You are level", self.level)


    #berechnet nächstes Level, evtl dann auf max Level anpassen
    def nextLevel(self, win_state):
        #global level
        if win_state == -1 and self.level > 0:
            self.level -= 1
            self.move.do_say(Sentence.LEVEL_DEC)
        elif win_state == 1 and self.level < 4:
            self.level += 1
            self.move.do_say(Sentence.LEVEL_INC)

    def show_level(self):
        if self.level == 0:
            self.move.do_animation(Animation.LEVEL0)
        elif self.level == 1:
            self.move.do_animation(Animation.LEVEL1)
        elif self.level == 2:
            self.move.do_animation(Animation.LEVEL2)
        elif self.level == 3:
            self.move.do_animation(Animation.LEVEL3)


    def who_starts(self):
        # check previous startplayer, if 0 -> first game -> random
        r = random.randint(1, 2)
        if self.first == 0:
            return r
        # check winhistory, if last one was a tie -> random, else the one who lost starts
        elif len(self.winHistory) > 0:
            if self.winHistory[-1] == 0:
                print(r, 'starts')
                return r
            elif self.winHistory[-1] == -1:
                print('Reachy starts')
                return 1
            else:
                print('Human starts')
                return 2


    def arcadeModus(self):
        h = True
        exit_game = "1"
        while exit_game == "1":
            self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            self.game_closed = False
            self.reachy_moveCounter = 0
            self.player_moveCounter = 0
            #self.first = input("who goes first? \n 1 for Reachy, 2 for Player: ")
            tmp = self.who_starts()
            self.first = tmp
            self.show_level()
            if self.first == 1:
                # reachy's first move
                self.move.do_animation(Animation.START_REACHY)
                self.board = Reachy.make_first_move(self.board,self.reachy_moveCounter, self.move)
                self.reachy_moveCounter = self.reachy_moveCounter + 1
                HI.print_board(self.board)
                self.play(self.move)
                exit_game = input("Press 1 to play again, Press any button to exit: ")
            elif self.first == 2:
                self.move.do_animation(Animation.START_OPPONENT)
                HI.print_board(self.board)
                self.play(self.move)
                exit_game = input("Press 1 to play again, Press any button to exit: ")
            else:
                print("input invalid")
        self.move.do_animation(Animation.SAD_ANTENNAS)




