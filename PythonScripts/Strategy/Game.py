import Human_Interaction as HI
import Computer_Player as Reachy

board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
reachy_score = 0
player_score = 0
reachy_moveCounter = 0
player_moveCounter = 0
level = 2

game_closed = False


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


# prüft, ob der neue Spielzustand legal ist
def check_board(input):
    global board, player_moveCounter
    # max ein neuer Stein
    new_piece = 0
    # alte Steine bleiben unverändert und kein Reachy-stein auf ein leeres Feld
    illegal_change = False
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0 and input[i][j] == -1:
                new_piece += 1
            elif board[i][j] != input[i][j]:
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
    board = input
    player_moveCounter += 1
    return True


# prüft, ob jemand gewonnen hat oder es unentschieden ist
def check_state():
    global game_closed
    global reachy_score
    global player_score

    for combo in range(len(wincombinations)):
        if combovalue(combo) == 3:
            print("Reachy won!")
            reachy_score = reachy_score + 1
            nextLevel(-1)
            game_closed = True
        elif combovalue(combo) == -3:
            print("Human won!")
            player_score = player_score + 1
            nextLevel(1)
            game_closed = True

    found_space = False
    for row in board:
        for cell in row:
            if cell == 0:
                found_space = True
    if not found_space:
        print("No more moves possible...")
        # nextLevel(0)
        game_closed = True


def play():
    global reachy_moveCounter, board
    while not game_closed:
        input = HI.make_user_move(board)
        if check_board(input) == True:
            check_state()
            if not game_closed:
                board = Reachy.make_computer_move(board, level, reachy_moveCounter, player_moveCounter)
                reachy_moveCounter += 1
                print("reachy moved {} times".format(reachy_moveCounter))
                check_state()
            HI.print_board(board)
    print("current score: Reachy ({}) : Player ({})".format(reachy_score, player_score))
    print("You are level", level)


#berechnet nächstes Level, evtl dann auf max Level anpassen
def nextLevel(win_state):
    global level
    if win_state == -1:
        level -= 1
        if level == -1:
            level = 0
    elif win_state == 1:
        level += 1
        if level == 3:
            level = 2


def arcadeModus():
    global level
    global game_closed
    global board
    global reachy_moveCounter
    global player_moveCounter
    h = True
    exit_game = "1"
    while exit_game == "1":
        board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        game_closed = False
        reachy_moveCounter = 0
        player_moveCounter = 0
        first = input("who goes first? \n 1 for Reachy, 2 for Player: ")
        if first == "1":
            # reachy's first move
            board = Reachy.make_first_move(board)
            reachy_moveCounter = reachy_moveCounter + 1
            HI.print_board(board)
            play()
            exit_game = input("Press 1 to play again, Press any button to exit: ")
        elif first == "2":
            HI.print_board(board)
            play()
            exit_game = input("Press 1 to play again, Press any button to exit: ")
        else:
            print("input invalid")


arcadeModus()

# board = [[0, -1, 0], [0, 1, 0], [0, 0, 0]]
# input = [[0, -1, 0], [1, 1, 0], [0, -1, 0]]
# print(check_board(input))




