from enum import Enum, unique


@unique
class Board(Enum):
    """
    Enum class representing the Tic Tac Toe board positions
    """
    TOP_LEFT = [0.28,0.3,0]
    TOP_CENTER = [0.284,0.175,0]
    TOP_RIGHT = [0.284,0.047,0]
    CENTER_LEFT = [0.166,0.3,0]
    CENTER = [0.166,0.175,0]
    CENTER_RIGHT = [0.166,0.047,0]
    BOTTOM_LEFT = [0.063,0.28,0]
    BOTTOM_CENTER = [0.063,0.175,0]
    BOTTOM_RIGHT = [0.063,0.047,0]

    
