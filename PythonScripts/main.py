from reachy_sdk import ReachySDK
from Movement import MoveFacade
from Perception import PerceptionFacade

reachy = ReachySDK("localhost")

move = MoveFacade(reachy)
perc = PerceptionFacade()

"""
strat = CStrategie()

perc.set_dependencies(reachy, move, strat)
move.set_dependencies(reachy, perc, strat)
strat.set_dependencies(reachy, move, perc)


strat.start_game()
"""