from square import Square
from board_detection.boardcases_pipeline import BoardcasesPipeline
from game_state_detection.boardcases_state_pipeline import BoardcasesStatePipeline
from reachy_sdk import ReachySDK
import yaml
import movement
import cv2
from stage import Stage
import time
from image_stability import ImageStability

config = yaml.safe_load(open("global_config.yml"))

def getHost():
    if config["stage"] == Stage.SIMULATION.value:
        return "localhost"
    elif config["stage"] == Stage.LAB.value:
        #Add Reachys Lab IP here
        return "Reachys Lab IP"
    
#reachy = ReachySDK(getHost())
reachy=True
"""
reachy.turn_on('head')
reachy.head.compliant = False
time.sleep(0.1)

# move head to goal position
movement.goal_position(reachy)
"""
stability = ImageStability(reachy)
stableImage = cv2.imread("board_detection/img1.png") #stability.isStable()

if len(stableImage) > 1:
    
    boardPipe = BoardcasesPipeline(stableImage, config["BOARDCOLOR_BOUNDS_LOWER"], config["BOARDCOLOR_BOUNDS_UPPER"])


    board_cases = boardPipe.getBoardCases()
    squares = []
    for square, values in board_cases.items():
        print(values)
        top_left = values[2]
        bottom_right = values[1]
        squares.append(Square(top_left[0], 
                                top_left[1], 
                                bottom_right[0], 
                                bottom_right[1], 
                                None))
    print(squares)

    statePipe = BoardcasesStatePipeline(reachy, squares)
    state = statePipe.get_board_cases()

    print(state)


"""
movement.base_position(reachy)
time.sleep(0.2)
reachy.head.compliant = True
"""