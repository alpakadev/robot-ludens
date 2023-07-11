from reachy_sdk import ReachySDK
from Movement.MoveFacade import MoveFacade
from Perception.PerceptionFacade import PerceptionFacade
from Strategy.StrategyFacade import StrategyFacade
from Movement.Enums import Outside
from Movement.Enums import Board
from Movement.Enums.Animation import Animation
from Movement.Enums.Sentence import Sentence
import time

reachy = ReachySDK("localhost")
#reachy = ReachySDK("192.168.1.94") # with_mobile_base = True)

move = MoveFacade()
perc = PerceptionFacade()
strat = StrategyFacade()

perc.set_dependencies(reachy, move, strat)
move.set_dependencies(reachy, perc, strat)
strat.set_dependencies(move, perc)

# If the the joints of reachy gets stuck, call this function
move.do_deactivate_reachys_joints()

## Calibration ##
## Calibrating real Reachy; Not needed in simulation
## For Calibration hold the middle of the right Hand
## on top of the bottem right corner of the board
# move.do_calibration()
# time.sleep(5) # Enough time, to move away after calibration

## Face Recognition ##
# time.sleep(3)
# Identify and save face of the person opposite of reachy
#perc.identify_human_player()
#perc.look_at_human_player() 
# Every call of look_at_human_player will cause delay of at least 2 seconds

# To ensure a safe arm position without collision with the blocks
move.do_safe_arm_pos()

## Block Detection ##
## Sets the mode to detecting unused blocks, instead of predefined marked positions
## Does not work reliably in simulation
# move.set_mode_to_detecting_blocks()

## Sounds ##
## Sounds will crash most of the time on Windows and Linux
## Should work on MacOS
move.set_mode_to_playing_sounds()


# Starting the Game
strat.start_game()

# move.do_say(Sentence.JOKE)





