import copy
import random
import Movement.Enums.Board as Board_enum  
import Movement.Enums.Outside as Outside_enum 
from Movement.MoveFacade import MoveFacade 


# Wahrscheinlichkeiten für bestimmte Züge abhängig vom Level
winning = {
    0: 25,
    1: 50,
    2: 90,
    3: 100
}

preventing = {
    0: 10,
    1: 50,
    2: 75,
    3: 100
}

trap = {
    0: 00,
    1: 40,
    2: 60,
    3: 100
}

good = {
    0: 20,
    1: 50,
    2: 75,
    3: 100
}


board_positions = {
    (0,1): Board_enum.Board.TOP_CENTER, 
    (0,0): Board_enum.Board.TOP_LEFT, 
    (0,2): Board_enum.Board.TOP_RIGHT, 
    (1,0): Board_enum.Board.CENTER_LEFT, 
    (1,1): Board_enum.Board.CENTER, 
    (1,2): Board_enum.Board.CENTER_RIGHT, 
    (2,0): Board_enum.Board.BOTTOM_LEFT ,
    (2,1): Board_enum.Board.BOTTOM_CENTER, 
    (2,2): Board_enum.Board.BOTTOM_RIGHT
}

block_positions = {
    1 : Outside_enum.Outside.BLOCK_1,
    2 : Outside_enum.Outside.BLOCK_2,
    3 : Outside_enum.Outside.BLOCK_3,
    4 : Outside_enum.Outside.BLOCK_4,
    5 : Outside_enum.Outside.BLOCK_5
}

board = []
level = 1
reachy_moveCounter = 0
player_moveCounter = 0
chosen = tuple()

# hier können die Zielkoordinaten für die Bewegung abgelegt werden
coordinates = []

# alle möglichen Gewinnkombinationen
wincombinations = [
    [[0,0], [0,1], [0,2]],
    [[1,0], [1,1], [1,2]],
    [[2,0], [2,1], [2,2]],

    [[0,0], [1,0], [2,0]],
    [[0,1], [1,1], [2,1]],
    [[0,2], [1,2], [2,2]],

    [[0,2], [1,1], [2,0]],
    [[0,0], [1,1], [2,2]]
]
corners = [
    [0,0], [0,2], [2,0], [2,2]
]


# berechnet die Summe der Einträge einer Gewinnkombination
def combovalue(k, b=board):
    if not b:
        b=board
    wert = b[wincombinations[k][0][0]][wincombinations[k][0][1]] + b[wincombinations[k][1][0]][wincombinations[k][1][1]] + b[wincombinations[k][2][0]][wincombinations[k][2][1]];
    return wert



# versuche zu gewinnen (2) oder einen Gewinn zu verhindern (-2)
def make_combo_move(n, p):
    global chosen
    # Gewinn verhindern nur mit gewisser Wahrscheinlichkeit
    if n == -2:
        if p < (100 - preventing[level]):
            return False
    # Gewinnen nur mit gewisser Wahrscheinlichkeit
    if n == 2:
        if p < (100 - winning[level]):
            return False
    #print("trying to make combo move")
    # prüfe, ob eine Kombination passt
    for combo in range(len(wincombinations)):
        if combovalue(combo) == n:
            # setze auf das freie Feld in der Kombination
            for i in range(3):
                if board[wincombinations[combo][i][0]][wincombinations[combo][i][1]] == 0:
                    board[wincombinations[combo][i][0]][wincombinations[combo][i][1]] = 1
                    chosen = (wincombinations[combo][i][0],wincombinations[combo][i][1])
                    return True
    return False

def boardtransformation():
    
    vierboard = []
    #Transformation des Boards (mit 4 statt -1)
    for k in range(3):
        teil = []
        for j in range(3):
            if board[k][j] == -1:
                teil.append(4)
            else:
                teil.append(board[k][j])
        vierboard.append(teil)
    return vierboard


def GKv1finden(vierboard):
    GKv1gefunden = []

    #Finden der GK mit Summe 1 (Belegung: 0 + 0 + 1) (Gkv1)
    for combo in range(len(wincombinations)):
        if combovalue(combo, vierboard) == 1:
            GKv1gefunden += (wincombinations[combo])
    return GKv1gefunden

def in001setzen(p):
    print("in001setzten vielleicht")
    global chosen
    # nur mit bestimmter Wahrscheinlichkeit guten Zug machen
    if p < (100 - good[level]):
        return False
    
    print("in001setzten")
    vierboard = boardtransformation()
    GKv1 = GKv1finden(vierboard)
    for feld in GKv1:
        if  board[feld[0]][feld[1]] == 0:
            #print("freies Feld: ", feld)
            board[feld[0]][feld[1]] = 1
            chosen = (feld[0],feld[1])
            print("hat wirklich geklappt")
            return True

def setup_trap(p):
    global chosen
    # Fallen stellen nur mit gewisser Wahrscheinlichkeit
    if p < (100 - trap[level]):
        return False
    #print("trying to setup trap")

    ## Problem: -1 + 1 + 1 == 0 + 0 + 1 == 1 
    #vierboard = []
    ##Transformation des Boards (mit 4 statt -1)
    #for k in range(3):
    #    teil = []
    #    for j in range(3):
    #        if board[k][j] == -1:
    #            teil.append(4)
    #        else:
    #            teil.append(board[k][j])
    #    vierboard.append(teil)
    #Problem solved
    #print(vierboard)
    vierboard = boardtransformation()

    ##Finden der GK mit Summe 1 (Belegung: 0 + 0 + 1) (Gkv1)
    #for combo in range(len(wincombinations)):
    #    if combovalue(combo, vierboard) == 1:
    #        GKv1 += (wincombinations[combo])
    #
    ##print(GKv1)
        ##GKv1 = [ [x,x],[x,x],[x,x], [x,x],[x,x],[x,x], [x,x],[x,x],[x,x] ]

    GKv1 = GKv1finden(vierboard)

    if len(GKv1) > 1: #and reachy_moveCounter > 1: weiter oben
        #Gemeinsames Feld zweier GKv1 finden
        for feld in GKv1:
            if GKv1.count(feld) > 1 and board[feld[0]][feld[1]] == 0:
                #print("freies gemeinsames Feld: ", feld)
                board[feld[0]][feld[1]] = 1
                chosen = (feld[0],feld[1])
                return True
    return False
          

def corner_move():
    global chosen
    #print("trying to make corner_move")
    free_corner = False
    for k in range(4):
        if board[corners[k][0]][corners[k][1]] == 0:
            free_corner = True
    while free_corner:
        i = random.randint(0, 3)
        if board[corners[i][0]][corners[i][1]] == 0:
            board[corners[i][0]][corners[i][1]] = 1
            chosen = (corners[i][0],corners[i][1])
            return True
    return False


def make_good_move(p):
    global chosen
    # nur mit bestimmter Wahrscheinlichkeit guten Zug machen
    if p < (100 - good[level]):
        return False
    #print("trying to make good move")

    if reachy_moveCounter == 0 and player_moveCounter == 1:
        # try the middle cell and make move if possible
        #print("Zug 1.1")
        if board[1][1] == 0:
            board[1][1] = 1
            chosen = (1,1)
            return True
        else:
            if corner_move():
                return True

    elif reachy_moveCounter == 1 and player_moveCounter == 1:
        #print("Zug 2.0")
        if corner_move():
            return True

    elif reachy_moveCounter == 1 and player_moveCounter == 2:
        # FALLE VERHINDERN
        #print("Zug 2.1")
        if combovalue(6) == -1 or combovalue(7) == -1:
            while 1:
                x = 1
                y = random.randint(0, 2)
                randfeld = [x, y]
                a = random.sample(randfeld, 2)
                if a != [1,1]:
                    
                    board[a[0]][a[1]] = 1
                    chosen = (a[0],a[1])
                    return True
    return False


def make_random_move():
    global chosen
    #print("trying to make random move")
    # generate new coordinates until a free spot is found and place the mark
    target = "start"
    while target != 0:
        # pick two random numbers between 0 and 2
        x = random.randint(0, 2)
        y = random.randint(0, 2)
        # make move if possible
        target = board[x][y]
    else:
        board[x][y] = 1
        chosen = (x,y)


def make_first_move(currentboard,reachy_moves, move: MoveFacade):
    global  reachy_moveCounter, chosen
    reachy_moveCounter = reachy_moves
    #print("trying to make first move")
    tmp_board = copy.deepcopy(currentboard)

    x = random.randint(0, 2)
    if x == 1:
        tmp_board[1][1] = 1
        chosen = (1,1)
    else:
        y = random.randint(0, 1)
        tmp_board[x][y * 2] = 1
        chosen = (x,y * 2)

    # Parameters to pass to team bewegung
    reachy_moveCounter = reachy_moveCounter + 1
    chosenmove =  board_positions[chosen]
    currentblock = block_positions[reachy_moveCounter]
    print(chosenmove , currentblock)
    move.do_move_block(from_enum=currentblock,to_enum=chosenmove)
    return tmp_board


# Funktion: Gegner macht auch strategisch gewichtet gute Züge
def make_computer_move(currentboard, currentlevel, reachy_moves, player_moves, move : MoveFacade):
    global board, level, reachy_moveCounter, player_moveCounter, chosen
    board = copy.deepcopy(currentboard)
    level = currentlevel
    reachy_moveCounter = reachy_moves
    player_moveCounter = player_moves
    # welcher Zug gemacht wird abh. von p
    p = random.randint(0, 100)
    if not make_combo_move(2, p):
        if not make_combo_move(-2, p):
            if not setup_trap(p):
                if not make_good_move(p):
                    if not in001setzen(p):
                        make_random_move()

    # Parameters to pass to team bewegung
    reachy_moveCounter = reachy_moveCounter + 1
    chosenmove =  board_positions[chosen]
    currentblock = block_positions[reachy_moveCounter]
    print(chosenmove , currentblock)
    move.do_move_block(currentblock,chosenmove)
    return board