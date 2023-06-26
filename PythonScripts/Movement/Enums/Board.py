from enum import Enum, unique


@unique
class Board(Enum):
    """
    Enum class representing the Tic Tac Toe board positions
    """
    TOP_LEFT = [0.25, 0.31, 0]
    TOP_CENTER = [0.25, 0.18, 0]
    TOP_RIGHT = [0.25, 0.08, 0]
    CENTER_LEFT = [0.16, 0.31, 0]
    CENTER = [0.16, 0.18, 0]
    CENTER_RIGHT = [0.16, 0.08, 0]
    BOTTOM_LEFT = [0.02, 0.29, 0]
    BOTTOM_CENTER = [0.02, 0.18, 0]
    BOTTOM_RIGHT = [0.02, 0.08, 0]
