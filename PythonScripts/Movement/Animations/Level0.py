import time
import random

def animation_level0(reachy):
    """
    indicating level 0: beginner
    """
    reachy.turn_on("head")

    reachy.head.l_antenna.goal_position = 60.0 
    reachy.head.r_antenna.goal_position = -70.0
    time.sleep(2.5)
    
    reachy.head.l_antenna.goal_position = 0.0
    reachy.head.r_antenna.goal_position = 0.0
    time.sleep(5.0)


   