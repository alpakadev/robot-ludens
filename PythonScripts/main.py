from reachy_sdk import ReachySDK
from Movement.MoveFacade import MoveFacade
from Perception.PerceptionFacade import PerceptionFacade
from Strategy.StrategyFacade import StrategyFacade
from Movement.Enums import Outside
from Movement.Enums import Board
from Movement.Enums.Animation import Animation
import time

reachy = ReachySDK("localhost")
# reachy = ReachySDK("192.168.1.94")

move = MoveFacade(reachy)
perc = PerceptionFacade(reachy)
strat = StrategyFacade()



perc.set_dependencies(move, strat)
move.set_dependencies(perc, strat)
strat.set_dependencies(move, perc)

#move.do_animation(Animation.HAPPY)

# If the Arm gets stuck, call this function
move.do_deactivate_right_arm()

# Calibrating real Reachy; Not needed in simulation
move.do_calibration()

# time.sleep(5)
# To ensure a safe arm position without collision with the blocks
# Outsource this as one command in MoveFacade
move.do_safe_arm_pos()

# Starting the Game
strat.start_game()
