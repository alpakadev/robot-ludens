""" main_real_reachy.py
This main file is designed to work with the real Reachy.
    - Please read the Commments in the Main-file first 
The activated modes are:
    + Calibration (Needed for the Real reachy)
    + Voice lines are played (Works on MacOS/Linux, crashes on Windows!)
    - No Face Recognition
    - No Outside Block Detection
Note:
    1. The Simulation runs with reachy-SDK version 0.4.0.
        - higher versions break the head movement 
    2. When connecting remotely to the real Reachy: 
        - required reachy-SDK 0.7.0
    3. When running on reachy:
        - Still Requires reachy-SDK 0.7.0
        - Reachy is beeing shipped with reachy-sdk 0.5.4,  
            which would break the head-movement
"""

import time

from Movement.Enums import Board, Outside
from Movement.Enums.Animation import Animation
from Movement.Enums.Sentence import Sentence
from Movement.MoveFacade import MoveFacade
from Perception.PerceptionFacade import PerceptionFacade
from reachy_sdk import ReachySDK
from Strategy.StrategyFacade import StrategyFacade

## Choose which connection address you want to use!
# reachy = ReachySDK("localhost")
reachy = ReachySDK("192.168.1.94")  # , with_mobile_base = True)

move = MoveFacade()
perc = PerceptionFacade()
strat = StrategyFacade()

perc.set_dependencies(reachy, move, strat)
move.set_dependencies(reachy, perc, strat)
strat.set_dependencies(move, perc)

# If the the joints of reachy gets stuck, call this function
# move.do_deactivate_reachys_joints()

## Calibration ##
## Calibrating real Reachy; Not needed in simulation
## For Calibration: hold the middle of the right Hand of reachy
## on top of the bottem right corner of the board
move.do_calibration()
time.sleep(5)  # Enough time, to move away after calibration
# Can utilize calibration coordinates from before
# move.do_set_origin([0.16, -0.25, -0.37])

## Face Recognition ##
# time.sleep(3)
# Identify and save face of the person opposite of reachy
# perc.identify_human_player()
# perc.look_at_human_player()
# Every call of look_at_human_player will cause delay of at least 2 seconds

## To ensure a safe arm position without collision with the blocks
## Always needed; Moves arm "above Block 5"
move.do_safe_arm_pos()

## Block Detection ##
## Sets the mode to detecting unused blocks, instead of predefined marked positions
## Does not work reliably in simulation, be cautious with real reachy
move.set_mode_to_detecting_blocks()

## Sounds ##
## Sounds will crash most of the time on Windows
## Should work on MacOS and linux (Ubuntu)
# move.set_mode_to_playing_sounds()


# Starting the Game
strat.start_game()
