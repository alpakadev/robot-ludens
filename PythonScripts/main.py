from reachy_sdk import ReachySDK
from Movement.MoveFacade import MoveFacade
from Perception.PerceptionFacade import PerceptionFacade
from Strategy.StrategyFacade import StrategyFacade
from Movement.Enums import Outside
from Movement.Enums import Board
from Movement.Enums.Animation import Animation
import time


reachy = ReachySDK("localhost")
#reachy = ReachySDK("192.168.1.94") # with_mobile_base = True) 

move = MoveFacade()
perc = PerceptionFacade(reachy)
strat = StrategyFacade()

perc.set_dependencies(move, strat)
move.set_dependencies(reachy, perc, strat)
strat.set_dependencies(move, perc)


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

# Testing animations

#move.do_animation(Animation.ANGRY) #fertig
#move.do_animation(Animation.CLUELESS) #fertig
#move.do_animation(Animation.DISAPPROVAL) #fertig
#move.do_animation(Animation.FORWARD) #mobile base ...
#move.do_animation(Animation.HAPPY_ANTENNAS)
#move.do_animation(Animation.LEVEL0)
#move.do_animation(Animation.LEVEL1) 
#move.do_animation(Animation.LEVEL2) 
#move.do_animation(Animation.LEVEL3)
#move.do_animation(Animation.LEVEL4)
#move.do_animation(Animation.LOSE) #fertig
#move.do_animation(Animation.SAD_ANTENNAS) #fertig
#move.do_animation(Animation.START_OPPONENT) #fertig
#move.do_animation(Animation.START_REACHY) #fertig
#move.do_animation(Animation.THINKING) #fertig
#TIE #fix TIE; its awfully wrong (dont try at reachy ONLY UNITY)
#move.do_animation(Animation.WIN) #fertig


#move.do_animation(Animation.INHALE)
