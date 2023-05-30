from reachy_sdk import ReachySDK
from Movement.MoveFacade import MoveFacade
from Perception.PerceptionFacade import PerceptionFacade
from Strategy.StrategyFacade import StrategyFacade

reachy = ReachySDK("192.168.1.94")

move = MoveFacade()
perc = PerceptionFacade(reachy)
strat = StrategyFacade()

perc.set_dependencies(move, strat)
move.set_dependencies(reachy, perc, strat)
strat.set_dependencies(move, perc)

move.do_calibration()
strat.start_game()

