from reachy_sdk import ReachySDK
from Movement import MoveFacade
from Perception import PerceptionFacade

reachy = ReachySDK("localhost")

move = MoveFacade(reachy)
perc = PerceptionFacade(reachy)

"""
strat = CStrategie()

perc.set_dependencies(move, strat)
move.set_dependencies(reachy, perc, strat)
strat.set_dependencies(reachy, move, perc)


strat.start_game()
"""