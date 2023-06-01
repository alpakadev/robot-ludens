import random
from enum import Enum, unique


@unique
class Outside(Enum):
    """
    Enum class representing the positions of the Tic Tac Toe blocks that Reachy can take and place.
    """
    #BLOCK_1 = [0.125, -0.085, 0.0]
    #BLOCK_2 = [0.125, -0.185, 0.0]
    #BLOCK_3 = [0.195, -0.085, 0.0]
    #BLOCK_4 = [0.195, -0.185, 0.0]
    #BLOCK_5 = [0.265, -0.085, 0.0]

    BLOCK_3 = [0.265, -0.085, 0.0]
    BLOCK_4 = [0.265, -0.185, 0.0]
    BLOCK_1 = [0.195, -0.085, 0.0]
    BLOCK_2 = [0.195, -0.185, 0.0]
    BLOCK_5 = [0.335, -0.085, 0.0]
