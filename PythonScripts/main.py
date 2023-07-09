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

# If the Arm gets stuck, call this function
move.do_deactivate_right_arm()

# Calibrating real Reachy; Not needed in simulation
# move.do_calibration()
# time.sleep(5) # Enough time, to move away after calibration

# To ensure a safe arm position without collision with the blocks
#move.do_safe_arm_pos()

# Sets the mode to detecting unused blocks, instead of predefined marked positions
# move.set_mode_to_detecting_blocks()

# Starting the Game
#strat.start_game()

#move.do_animation(Animation.)
move.do_say(Sentence.CHANCE_HM)
time.sleep(3)
move.do_say(Sentence.CHANCE_RH)
time.sleep(3)
move.do_say(Sentence.DETECT_TIE)
time.sleep(3)
move.do_say(Sentence.ILLEGALMOVE_HM)
time.sleep(3)
move.do_say(Sentence.ILLEGALMOVE_RH)
time.sleep(3)
move.do_say(Sentence.JOKE)
time.sleep(3)
move.do_say(Sentence.LEVEL_DEC)
time.sleep(3)
move.do_say(Sentence.NEXT_MOVE_HM)
time.sleep(3)
move.do_say(Sentence.NEXT_MOVE_RH)
time.sleep(3)
move.do_say(Sentence.LEVEL_INC)
time.sleep(3)
move.do_say(Sentence.TRAP_DONE_RH)
time.sleep(3)
move.do_say(Sentence.TRAP_RECOGNIZE)
time.sleep(3)
move.do_say(Sentence.WIN_PREVENT)
time.sleep(3)
move.do_say(Sentence.ILLEGALMOVE_HM)
time.sleep(3)
move.do_say(Sentence.WIN_PREVENT_FAILED)
time.sleep(3)
move.do_say(Sentence.WAITING)
time.sleep(3)
