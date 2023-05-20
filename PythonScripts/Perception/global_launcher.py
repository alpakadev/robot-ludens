from game_state_detection.game_figure_detection import get_all_pieces_coordinates
from game_state_detection.game_state_detection import get_board_state
from game_state_detection.board_cases_detection import get_board_cases
from game_state_detection.game_board_detection import game_board_detection
from reachy_sdk import ReachySDK
import yaml
import movement
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

if config["stage"] != Stage.TESTING.value:
    reachy.turn_on('head')
    reachy.head.compliant = False
    time.sleep(0.1)
    movement.goal_position(reachy)

stability = ImageStability(reachy)
stableImage = stability.isStable()

if len(stableImage) > 1:
    game_board_coords = game_board_detection(stableImage)
    cases_coords = get_board_cases(game_board_coords)

    red_figure_coords, green_figure_coords = get_all_pieces_coordinates(stableImage, game_board_coords)
    game_score = get_board_state(stableImage, cases_coords)
    print(game_score)

if config["stage"] != Stage.TESTING.value:
    movement.base_position(reachy)
    time.sleep(0.2)
    reachy.head.compliant = True