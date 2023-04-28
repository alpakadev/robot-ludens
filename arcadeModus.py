import random

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

#   for i in range(0, 3):
#       if (board[i][0] + board[i][1] + board[i][2]) == 3:
#           game_closed = True
#          print("Reachy won!")
#       elif (board[i][0] + board[i][1] + board[i][2]) == -3:
#           game_closed = True
#           print("You won!")
#       elif (board[0][i] + board[1][i] + board[2][i]) == 3:
#           game_closed = True
#           print("Reachy won!")
#       elif (board[0][i] + board[1][i] + board[2][i]) == -3:
#           game_closed = True
#           print("You won!")
#   if board[0][0] + board[1][1] + board[2][2] == 3:
#       game_closed = True
#       print("Reachy won!")
#   elif board[0][0] + board[1][1] + board[2][2] == -3:
#       game_closed = True
#       print("You won!")
#   elif board[0][2] + board[1][1] + board[2][0] == 3:
#       game_closed = True
#       print("Reachy won!")
#   elif board[0][2] + board[1][1] + board[2][0] == -3:
#       game_closed = True
#       print("You won!")

    found_space = False
    for row in board:
        for cell in row:
            if cell == 0:
                found_space = True
    if not found_space:
        print("No more moves possible...")
        game_closed = True
        checkNextLevel(0)

#winning move coordinates ermitteln
def check_chance():
    for combo in range(len(wincombinations)):
        if combovalue(combo) == 2:
            for i in range(3):
                if board[wincombinations[combo][i][0]][wincombinations[combo][i][1]] == 0:
                    return wincombinations[combo][i][0], wincombinations[combo][i][1]

#preventing move coordinates ermitteln
def check_risk():
    for combo in range(len(wincombinations)):
        if combovalue(combo) == -2:
            for i in range(3):
                if board[wincombinations[combo][i][0]][wincombinations[combo][i][1]] == 0:
                    return wincombinations[combo][i][0], wincombinations[combo][i][1]

#    for i in range(0, 3):
#        if (board[i][0] + board[i][1] + board[i][2]) == -2:
#            return i, board[i].index(0)
#        elif (board[0][i] + board[1][i] + board[2][i]) == -2:
#            for j in range(0, 3):
#                if board[j][i] == 0:
#                    return j, i
#    if board[0][0] + board[1][1] + board[2][2] == -2:
#        for k in range(0, 3):
#            if board[k][k] == 0:
#                return k, k
#    elif board[0][2] + board[1][1] + board[2][0] == -2:
#        for k in range(0, 3):
#            if board[k][2-k] == 0:
#                return k, 2-k



def make_winning_move(p):
    # Wahrscheinlichkeit, einen Winningmove zu machen, falls möglich ist bei 80%
    if p < (100-winning[level]):
        return False
    print('try winning move')
    coordinates = check_chance()
    if coordinates:
        print("found a chance")
        a = coordinates[0]
        b = coordinates[1]

        board[a][b] = 1
        check_state()
        return True
    else:
        return False


def make_preventing_move(p):
    if p < (100-preventing[level]):
        return False
    print('try prevent move')
    coordinates = check_risk()
    if coordinates:
        print("found a risk")
        a = coordinates[0]
        b = coordinates[1]

        board[a][b] = 1
        check_state()
        return True
    else:
        return False


def make_good_move(p):
    if p < (100-good[level]):
        return False
    print('try good move')
    # try the middle cell and make move if possible
    if board[1][1] == 0:
        board[1][1] = 1
        check_state()
        return True
    # else try to get into a corner cell
    else:
        if board[0][0] == 0 or board[0][2] == 0 or board[2][0] == 0 or board[2][2] == 0:
            print("picking a corner")
            while 1 != 0:
                x = random.randint(0, 3)
                if x == 0 and board[0][0] == 0:
                    board[0][0] = 1
                    check_state()
                    return True
                elif x == 1 and board[0][2] == 0:
                    board[0][2] = 1
                    check_state()
                    return True
                elif x == 2 and board[2][0] == 0:
                    board[2][0] = 1
                    check_state()
                    return True
                elif x == 3 and board[2][2] == 0:
                    board[2][2] = 1
                    check_state()
                    return True
        else:
            return False


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


# Funktion: Gegner macht auch strategisch gewichtet gute Züge
def make_computer_move():
    p = random.randint(0, 100)
    print("p: ", str(p))
    if not make_winning_move(p):
        if not make_preventing_move(p):
            if not make_good_move(p):
                make_random_move()


def make_user_move(coordinates):
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
        return True

#verschiedene Level (noch nicht richtig)
def level2Move():
    if not make_winning_move():
        if not make_preventing_move():
            if not make_good_move():
                make_random_move()


def level1Move():
    if not make_winning_move():
        if not make_preventing_move():
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


def arcadeModus():
    global level
    global game_closed
    global board
    h = True
    move = ""
    while h:
        print("You are now level", level)
        print_board()
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
            print_board()
        game_closed = False
        board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

arcadeModus()