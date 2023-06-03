from reachy_sdk import ReachySDK
from Movement.MoveFacade import MoveFacade
from Perception.PerceptionFacade import PerceptionFacade
from Strategy.StrategyFacade import StrategyFacade
from Movement.Enums import Outside
from Movement.Enums import Board

reachy = ReachySDK("localhost")

move = MoveFacade()
perc = PerceptionFacade(reachy)
strat = StrategyFacade()

perc.set_dependencies(move, strat)
move.set_dependencies(reachy, perc, strat)
strat.set_dependencies(move, perc)

 # If the Arm is stuck call this function

#move.do_calibration()
move.do_activate_right_arm()
move.do_right_angled_position()
strat.start_game()

#move.do_deactivate_right_arm()