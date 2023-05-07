from enum import Enum, unique


@unique
class Board(Enum):
    """
    Enum class representing the Tic Tac Toe board positions
    """
    TOP_LEFT = (0, 0, 0.1)
    TOP_CENTER = (0, 0, 0.2)
    TOP_RIGHT = (0, 0, 0.3)
    CENTER_LEFT = (0, 0, 0.4)
    CENTER = (0, 0, 0.5)
    CENTER_RIGHT = (0, 0, 0.6)
    BOTTOM_LEFT = (0, 0, 0.7)
    BOTTOM_CENTER = (0, 0, 0.8)
    BOTTOM_RIGHT = (0, 0, 0.9)
