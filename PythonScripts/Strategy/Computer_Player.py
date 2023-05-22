import copy
import random

# Wahrscheinlichkeiten für bestimmte Züge abhängig vom Level
winning = {
    0: 10,
    1: 50,
    2: 100
}

preventing = {
    0: 10,
    1: 50,
    2: 100
}

good = {
    0: 20,
    1: 50,
    2: 100
}

board = []
level = 1
reachy_moveCounter = 0
player_moveCounter = 0

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
def combovalue(k):
    wert = board[wincombinations[k][0][0]][wincombinations[k][0][1]] + board[wincombinations[k][1][0]][wincombinations[k][1][1]] + board[wincombinations[k][2][0]][wincombinations[k][2][1]];
    return wert


# versuche zu gewinnen (2) oder einen Gewinn zu verhindern (-2)
def make_combo_move(n, p):
    # Gewinn verhindern nur mit gewisser Wahrscheinlichkeit
    if n == -2:
        if p < (100 - preventing[level]):
            return False
    # Gewinnen nur mit gewisser Wahrscheinlichkeit
    if n == 2:
        if p < (100 - winning[level]):
            return False
    print("trying to make combo move")
    # prüfe, ob eine Kombination passt
    for combo in range(len(wincombinations)):
        if combovalue(combo) == n:
            # setze auf das freie Feld in der Kombination
            for i in range(3):
                if board[wincombinations[combo][i][0]][wincombinations[combo][i][1]] == 0:
                    board[wincombinations[combo][i][0]][wincombinations[combo][i][1]] = 1
                    return True
    return False

def setup_trap():
    print("trying to setup trap")

    # Problem: -1 + 1 + 1 == 1
    # board[]: [[x,x,x],
    #           [x,x,x],
    #           [x,x,x]]

    einDboard = []

    #Transformation des Boards (eindimensional mit 4 statt -1)
    for k in range(3):
        for j in range(3):
            if board[k][j] == -1:
                einDboard.append(4)
            else:
                einDboard.append(board[k][j])

        # einDboard = [x,x,x,x,x,x,x,x]
        #Problem solved

    GKv1 = []

    #Finden der GK mit Summe 1 (Belegung: 0 + 0 + 1) (Gkv1)
    for combo in range(len(wincombinations)):
        if combovalue(combo) == 1:
            GKv1.append(wincombinations[combo])

    print(GKv1)
        #GKv1 = [ [[x,x],[x,x],[x,x]], [[x,x],[x,x],[x,x]], [[x,x],[x,x],[x,x]] ]

    if len(GKv1) > 1: #and reachy_moveCounter > 1
        #Gemeinsames Feld zweier GKv1 finden
        for k in range(len(GKv1) - 1):
            for j in range(3):
                for i in range(k+1, len(GKv1)):
                    for h in range(3):
                        if GKv1[k][j] == GKv1[i][h] and board[GKv1[k][j][0]][GKv1[k][j][1]] == 0:
                            print("k=",k, "j=",j)
                            board[k][j] == 1
                            return True
    return False            

def corner_move():
    print("trying to make corner_move")
    free_corner = False
    for k in range(4):
        if board[corners[k][0]][corners[k][1]] == 0:
            free_corner = True
    while free_corner:
        i = random.randint(0, 3)
        if board[corners[i][0]][corners[i][1]] == 0:
            board[corners[i][0]][corners[i][1]] = 1
            return True
    return False


def make_good_move(p):
    # nur mit bestimmter Wahrscheinlichkeit guten Zug machen
    if p < (100 - good[level]):
        return False
    print("trying to make good move")

    if reachy_moveCounter == 0 and player_moveCounter == 1:
        # try the middle cell and make move if possible
        print("Zug 1.1")
        if board[1][1] == 0:
            board[1][1] = 1
            return True
        else:
            if corner_move():
                return True

    elif reachy_moveCounter == 1 and player_moveCounter == 1:
        print("Zug 2.0")
        if corner_move():
            return True

    elif reachy_moveCounter == 1 and player_moveCounter == 2:
        # FALLE VERHINDERN
        print("Zug 2.1")
        if combovalue(6) == -1 or combovalue(7) == -1:
            while 1:
                x = 1
                y = random.randint(0, 2)
                randfeld = [x, y]
                a = random.sample(randfeld, 2)
                if a != [1,1]:
                    print(a)
                    board[a[0]][a[1]] = 1
                    return True
    # TODO: Zug == 2.1: bei 4+1+4:Rand Feld, sonst Gewinnkombination mit Summe = 1 = 1+0+0

    return False


def make_random_move():
    print("trying to make random move")
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


def make_first_move(currentboard):
    print("trying to make first move")
    tmp_board = copy.deepcopy(currentboard)

    x = random.randint(0, 2)
    if x == 1:
        tmp_board[1][1] = 1
    else:
        y = random.randint(0, 1)
        tmp_board[x][y * 2] = 1
    return tmp_board


# Funktion: Gegner macht auch strategisch gewichtet gute Züge
def make_computer_move(currentboard, currentlevel, reachy_moves, player_moves):
    global board, level, reachy_moveCounter, player_moveCounter
    board = copy.deepcopy(currentboard)
    level = currentlevel
    reachy_moveCounter = reachy_moves
    player_moveCounter = player_moves
    # welcher Zug gemacht wird abh. von p
    p = random.randint(0, 100)
    if not make_combo_move(2, p):
        if not make_combo_move(-2, p):
            if not setup_trap():
                if not make_good_move(p):
                    make_random_move()
    reachy_moveCounter = reachy_moveCounter + 1
    return board