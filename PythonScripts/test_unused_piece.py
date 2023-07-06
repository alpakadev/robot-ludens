from reachy_sdk import ReachySDK
from Movement.MoveFacade import MoveFacade
from Perception.PerceptionFacade import PerceptionFacade
from Strategy.StrategyFacade import StrategyFacade
import time

# reachy = ReachySDK("localhost")
reachy = ReachySDK("192.168.1.94") # with_mobile_base = True) 

move = MoveFacade()
perc = PerceptionFacade()
strat = StrategyFacade()

perc.set_dependencies(reachy, move, strat)
move.set_dependencies(reachy, perc, strat)
strat.set_dependencies(move, perc)

move.do_move_head(look_at=[0.5, 0, -0.6])

starttime = time.time()

while True:
    if time.time() - starttime >= 5:
        nearest_unused_piece = perc.perception_implementation.get_nearest_unused_piece(move)        
        starttime = time.time()