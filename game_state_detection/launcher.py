'''
This is the test script that needs to be executed
in order to test Reachys ability to detect colors.

After starting the script, you can stop it by pressing q.
'''

from reachy_sdk import ReachySDK
import time
from movement import goal_position, base_position
from game_board_detection import game_board_detection # return game board and case coordinates
from cases_detection import cases_detection # return case coordinates
from game_figure_detection import game_figure_detection # returns figure colors and coordinates
from game_score_detection import game_score_detection # returns 3x3 array with 0,1,-1
from movement_detection import movement_detection # returns movement
import yaml
from stage import Stage
# config = yaml.safe_load(open("wahrnehmung/config.yml"))

# def getHost():
#     if config["stage"] == Stage.SIMULATION.value:
#         return "localhost"
#     elif config["stage"] == Stage.LAB.value:
#         #Add Reachys Lab IP here
#         return "Reachys Lab IP"

def main():
    # initialize Reachy
    reachy = ReachySDK("localhost")
    reachy.turn_on('head')
    reachy.head.compliant = False
    time.sleep(0.1)

    # move head to goal position
    goal_position(reachy)

    game_board_coords = game_board_detection(reachy)
    cases_coords = cases_detection(reachy)
    red_figure_coords, green_figure_coords = game_figure_detection(reachy, game_board_coords)
    game_score = game_score_detection(cases_coords, red_figure_coords, green_figure_coords)

    # movement_detection(reachy, game_board_coords)

    # move head to base position
    base_position(reachy)
    time.sleep(0.2)
    reachy.head.compliant = True


if __name__ == '__main__':
    main()