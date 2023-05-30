from reachy_sdk import ReachySDK
from Movement.MoveFacade import MoveFacade
from Perception.PerceptionFacade import PerceptionFacade
from Strategy.StrategyFacade import StrategyFacade

reachy = ReachySDK("localhost")

move = MoveFacade()
perc = PerceptionFacade(reachy)
strat = StrategyFacade()

perc.set_dependencies(move, strat)
move.set_dependencies(reachy, perc, strat)
strat.set_dependencies(move, perc)

<<<<<<< Updated upstream
=======
move.do_calibration()

move.do_move_head([0.5,0,-0.6])
#strat.start_game()
>>>>>>> Stashed changes

strat.start_game()
