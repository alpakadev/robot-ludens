import time

def animation_level0(reachy):
    reachy.turn_on("head")
    reachy.head.l_antenna.goal_position = -40.0 #level0
    reachy.head.r_antenna.goal_position = -40.0
    time.sleep(2.5)
    reachy.head.l_antenna.goal_position = 0.0
    reachy.head.r_antenna.goal_position = 0.0
    time.sleep(5.0)
    
   
   