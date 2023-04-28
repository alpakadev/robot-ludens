import random

reachy_moveCounter = 0
player_moveCounter = 0
board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
game_closed = False
level = 2


# Funktion: Spielbrett darstellen
def print_board():
    print("   -A---B---C-")
    i = 1
    for row in board:
        print(str(i) + " | " + str(row[0]) + " | " + str(row[1]) + " | " + str(row[2]) + " | ")
        print("   -----------")
        i += 1

# übersetzt user-spalten-input in index der Zelle
column = {
    'A': 0,
    'B': 1,
    'C': 2,
}

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


#berechnet die Summe der Einträge einer Gewinnkombination
def combovalue(k):
    wert = board[wincombinations[k][0][0]][wincombinations[k][0][1]] + board[wincombinations[k][1][0]][wincombinations[k][1][1]] + board[wincombinations[k][2][0]][wincombinations[k][2][1]];
    return wert

# prüft für jede Gewinnkombination, ob ein Sieg vorliegt
def check_state():
    global game_closed

    for combo in range(len(wincombinations)):
        if combovalue(combo) == 3:
            print("Reachy won!")
            game_closed = True
            checkNextLevel(-1)
        elif combovalue(combo) == -3:
            print("You won!")
            game_closed = True
            checkNextLevel(1)
    found_space = False
    for row in board:
        for cell in row:
            if cell == 0:
                found_space = True
    if not found_space:
        print("No more moves possible...")
        game_closed = True
        checkNextLevel(0)


#versuche zu gewinnen (2) oder einen Gewinn zu verhindern (-2)
def make_easy_move(n,p):
    if p < (100-preventing[level]):
        return False
    print('try prevent/winning move')
    #prüfe ob eine Kombination passt
    for combo in range(len(wincombinations)):
        if combovalue(combo) == n:
            #setze auf das freie Feld in der Kombination
            for i in range(3):
                if board[wincombinations[combo][i][0]][wincombinations[combo][i][1]] == 0:
                    board[wincombinations[combo][i][0]][wincombinations[combo][i][1]] = 1
                    return True
    return False


def make_good_move(p):
    if p < (100-good[level]):
        return False
    print('try good move')
    if reachy_moveCounter == 0 and player_moveCounter == 1:
        # try the middle cell and make move if possible
        if board[1][1] == 0:
            board[1][1] = 1
            check_state()
            return True
        else:
            corner_move()
            return True
            
    elif reachy_moveCounter == 1 and player_moveCounter == 1:
        print("CORNER MOVE")
        corner_move()
        return True

    elif reachy_moveCounter == 1 and player_moveCounter == 2:
        #FALLE VERHINDERN
        print("HIER!!")
        if combovalue(6) == -1 or combovalue(7) == -1:
            x = 1
            y = random.randint(0, 2)
            randfeld = [x,y]
            a = random.sample(randfeld,2)
            board[a[0]][a[1]] = 1
            return True

def corner_move():
    c = 1
    while c == 1:
        i = random.randint(0, 4)
        if board[corners[i][0]][corners[i][1]] == 0:
            board[corners[i][0]][corners[i][1]] = 1
            check_state()
            return True

def make_random_move():
    print('random move')
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
        check_state()

def make_first_move():
    x = random.randint(0,2)
    if x == 1:
        board[1][1] = 1
    else:
        y = random.randint(0,1)
        board[x][y*2] = 1

# Funktion: Gegner macht auch strategisch gewichtet gute Züge
def make_computer_move():
    p = random.randint(0, 100)
    print("p: ", str(p))
    if not make_easy_move(2,p):
        if not make_easy_move(-2,p):
            if not make_good_move(p):
                make_random_move()


def make_user_move(coordinates):
    global player_moveCounter
    # validate coordinates
    try:
        a = int(coordinates[0]) - 1
        b = column[coordinates[1].upper()]
    except:
        print("Please provide one digit between 1 and 3 followed by one character between A and C.")
        return False
    # check if place is empty
    target = board[a][b]
    if target != 0:
        print("The spot is already taken. Choose another.")
        return False
    else:
        board[a][b] = -1
        check_state()
        player_moveCounter = player_moveCounter + 1
        return True

#TODO: verschiedene Level (noch nicht richtig)
def level2Move():
    if not make_easy_move(2):
        if not make_easy_move(-2):
            if not make_good_move():
                make_random_move()

#TODO: verschiedene Level (noch nicht richtig)
def level1Move():
    if not make_easy_move(2):
        if not make_easy_move(-2):
            make_random_move()


def level0Move():
    make_random_move()

#berechnet nächstes Level, evtl dann auf max Level anpassen
def checkNextLevel(win_state):
    global level
    if win_state == -1:
        level = level - 1
        if level == -1:
            level = 0
    elif win_state == 1:
        level = level + 1
        if level == 3:
            level = 2


def play():
    global reachy_moveCounter 
    move = ''
    while move != "stop" and not game_closed:
        move = input("Chose the coordinates for your next move (i.g '1B'): ")
        # validate coordinate
        if make_user_move(move) and not game_closed:
            make_computer_move()
            ''' 
            if level == 0:
                level0Move()
            elif level == 1:
                level1Move()
            elif level == 2:
            # level2Move()
            '''
        print("reachy moved {} times".format(reachy_moveCounter))
        print_board()


def arcadeModus():
    global level
    global game_closed
    global board
    exit_game = "1"

    while exit_game == "1":
        board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        game_closed = False
        reachy_moveCounter = 0
        player_moveCounter = 0

        first = input ("who goes first? \n 1 for Reachy, 2 for Player: ")
        if first == "1":
            #reachy's first move
            make_first_move()
            reachy_moveCounter = reachy_moveCounter + 1
            print_board()
            play()
            exit_game = input("Press 1 to play again, Press any button to exit: ")
        elif first == "2":
            print_board()
            play()
            exit_game = input("Press 1 to play again, Press any button to exit: ")
        else:
            print("input invalid")

arcadeModus()