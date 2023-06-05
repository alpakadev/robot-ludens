from enum import Enum, unique


@unique
class Board(Enum):
    """
    Enum class representing the Tic Tac Toe board positions
    """
    TOP_LEFT = [0.27, 0.29, 0]
    TOP_CENTER = [0.27, 0.16, 0]
    TOP_RIGHT = [0.27, 0.06, 0]
    CENTER_LEFT = [0.18, 0.29, 0]
    CENTER = [0.18, 0.16, 0]
    CENTER_RIGHT = [0.18, 0.06, 0]
    BOTTOM_LEFT = [0.02, 0.27, 0]
    BOTTOM_CENTER = [0.02, 0.16, 0]
    BOTTOM_RIGHT = [0.02, 0.06, 0]
