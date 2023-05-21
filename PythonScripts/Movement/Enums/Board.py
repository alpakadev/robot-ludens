from enum import Enum, unique


@unique
class Board(Enum):
    """
    Enum class representing the Tic Tac Toe board positions
    """
    TOP_LEFT = [0, 0, 0.1]
    TOP_CENTER = [0, 0, 0.2]
    TOP_RIGHT = [0, 0, 0.3]
    CENTER_LEFT = [0, 0, 0.4]
    CENTER = [0, 0, 0.5]
    CENTER_RIGHT = [0, 0, 0.6]
    BOTTOM_LEFT = [0, 0, 0.7]
    BOTTOM_CENTER = [0, 0, 0.8]
    BOTTOM_RIGHT = [0, 0, 0.9]

    HAND_ROTATIONS = {
        TOP_LEFT: 45,
        TOP_CENTER: 45,
        TOP_RIGHT: 0,
        CENTER_LEFT: 45,
        CENTER: 45,
        CENTER_RIGHT: 0,
        BOTTOM_LEFT: 90,
        BOTTOM_CENTER: 90,
        BOTTOM_RIGHT: 45,
    }

    #Vectors from (0|0) (Bottom right corner of board)
    
    V_TOP_LEFT = (0.284,0.179,0)
    V_TOP_CENTER = (0.284,0.112,0)
    V_TOP_RIGHT = (0.284,0.047,0)
    V_CENTER_LEFT = (0.166,0.179,0)
    V_CENTER = (0.166,0.112,0)
    V_CENTER_RIGHT = (0.166,0.047,0)
    V_BOTTOM_LEFT = (0.063,0.179,0)
    V_BOTTOM_CENTER = (0.063,0.112,0)
    V_BOTTOM_RIGHT = (0.063,0.047,0)
    
