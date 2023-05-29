import copy
from Movement.MoveFacade import MoveFacade 
from Perception.PerceptionFacade import PerceptionFacade

# übersetzt user-spalten-input in index der Zelle
column = {
    'A': 0,
    'B': 1,
    'C': 2,
}


def print_board(board):
    print("   -A---B---C-")
    i = 1
    for row in board:
        print(str(i) + " | " + str(row[0]) + " | " + str(row[1]) + " | " + str(row[2]) + " | ")
        print("   -----------")
        i += 1


def make_user_move(board):
    # prüfe, ob der input Koordinaten enthält
    invalid = True
    new_board = copy.deepcopy(board)
    while invalid:
        try:
            coordinates = input("Chose the coordinates for your next move (i.g '1B'): ")
            a = int(coordinates[0]) - 1
            b = column[coordinates[1].upper()]
            new_board[a][b] = -1
            return new_board
        except:
            print("Please provide one digit between 1 and 3 followed by one character between A and C.")

def make_user_move_unity(board, perc : PerceptionFacade):
    invalid = True
    new_board = copy.deepcopy(board)
    while invalid:
        try:
            new_board = perc.get_game_state()
            print(new_board)
            return new_board
        except:
            print("waiting for input")
