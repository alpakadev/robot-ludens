from enum import Enum, unique


@unique
class Board(Enum):
    """
    Enum class representing the Tic Tac Toe board positions
    """
    TOP_LEFT = [0.32, 0.32, 0]
    TOP_CENTER = [0.32, 0.175, 0]
    TOP_RIGHT = [0.32, 0.07, 0]
    CENTER_LEFT = [0.166, 0.35, 0]
    CENTER = [0.196, 0.165, 0]
    CENTER_RIGHT = [0.196, 0.06, 0]
    BOTTOM_LEFT = [0.08, 0.28, 0]
    BOTTOM_CENTER = [0.04, 0.16, 0]
    BOTTOM_RIGHT = [0.09, 0.047, 0]
