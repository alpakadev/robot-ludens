from game_state_detection.game_score_detection import game_score_detection
from game_state_detection.game_figure_detection import game_figure_detection
from game_state_detection.cases_detection import cases_detection
from game_state_detection.game_board_detection import game_board_detection
from square import Square
from board_detection.boardcases_pipeline import BoardcasesPipeline
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
    else:
        return "localhost"
    
reachy = ReachySDK(getHost())
reachy=True
if config["stage"] != Stage.TESTING.value:
    reachy.turn_on('head')
    reachy.head.compliant = False
    time.sleep(0.1)

    # move head to goal position
    movement.goal_position(reachy)

stability = ImageStability(reachy)
stableImage = cv2.imread("Pipeline Bilder/img1.png") #stability.isStable()

if len(stableImage) > 1:
    
    boardPipe = BoardcasesPipeline(config["color_bounds"]["board_lower"], config["color_bounds"]["board_upper"])

    board_cases = boardPipe.getBoardCases(stableImage)

    # game_board_coords AND cases_coords SHOULD BE RETURNED FROM board_cases, 
    # I used my own test functions here
    game_board_coords = game_board_detection(reachy)
    cases_coords = cases_detection(reachy)


    red_figure_coords, green_figure_coords = game_figure_detection(reachy, game_board_coords)
    game_score = game_score_detection(cases_coords, red_figure_coords, green_figure_coords)

if config["stage"] != Stage.TESTING.value:
    movement.base_position(reachy)
    time.sleep(0.2)
    reachy.head.compliant = True