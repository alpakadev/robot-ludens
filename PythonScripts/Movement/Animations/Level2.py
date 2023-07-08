import time

def animation_level2(reachy):
    """
    indicating level 2: intermediate 
    """
    reachy.turn_on("head")
    
    reachy.head.l_antenna.goal_position = -50.0 
    reachy.head.r_antenna.goal_position = 50.0
    time.sleep(2.5)

    reachy.head.l_antenna.goal_position = 0.0
    reachy.head.r_antenna.goal_position = 0.0
    time.sleep(5.0)
    
    
