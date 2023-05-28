from reachy_sdk import ReachySDK
from Movement import MoveFacade
from Perception import PerceptionFacade
from Strategy import StrategyFacade

reachy = ReachySDK("localhost")

move = MoveFacade()
perc = PerceptionFacade(reachy)
strat = StrategyFacade()

perc.set_dependencies(move, strat)
move.set_dependencies(reachy, perc, strat)
strat.set_dependencies(reachy, move, perc)


strat.start_game()
