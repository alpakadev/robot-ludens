import random

board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
game_closed = False
reachy_score = 0
player_score = 0
reachy_moveCounter = 0
player_moveCounter = 0

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
    global reachy_score
    global player_score

    for combo in range(len(wincombinations)):
        if combovalue(combo) == 3:
            print("Reachy won!")
            game_closed = True
            reachy_score = reachy_score + 1
        elif combovalue(combo) == -3:
            print("You won!")
            game_closed = True
            player_score = player_score + 1

    found_space = False
    for row in board:
        for cell in row:
            if cell == 0:
                found_space = True
    if not found_space:
        print("No more moves possible...")
        game_closed = True

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

def make_winning_move():
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


def make_preventing_move():
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


def make_good_move():
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
    if not make_winning_move():
        if not make_preventing_move():
            if not make_good_move():
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

def play():
    global reachy_moveCounter
    global player_moveCounter
    move = ''
    while move != "stop" and not game_closed:
        move = input("Chose the coordinates for your next move (i.g '1B'): ")
        # validate coordinate
        if make_user_move(move) and not game_closed:
            player_moveCounter = player_moveCounter + 1
            make_computer_move()
            reachy_moveCounter = reachy_moveCounter + 1 
        print("reachy moved {} times".format(reachy_moveCounter))
        print_board()
    print("current score: Reachy ({}) : Player ({})".format(reachy_score,player_score))


exit_game = "1"
while exit_game == "1":
    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    game_closed = False
    first = input ("who goes first? \n 1 for Reachy, 2 for Player: ")
    if first == "1":
        #reachy's first move
        make_random_move()
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
    