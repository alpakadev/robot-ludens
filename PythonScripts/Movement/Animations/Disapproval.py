import time
import random


def animation_disapproval(reachy):
    """
    head shaking with changing antennas 
    """
    reachy.turn_on("head")
    reachy.head.look_at(0.05, 0, -0.03, 1.0)  
    time.sleep(0.5)

    reachy.head.r_antenna.speed_limit = 90.0
    reachy.head.l_antenna.speed_limit = 90.0

    reachy.head.r_antenna.goal_position = -45.0
    reachy.head.l_antenna.goal_position = 65.0
    time.sleep(1.5)

    reachy.head.look_at(0.05, 0, 0, duration=0.5,)

    # Head shaking

    for i in range(3):
        degree = random.randint(50,80) #randomized degree for antennas
       
        reachy.head.l_antenna.speed_limit = 40.0
        reachy.head.r_antenna.speed_limit = 40.0
        
        reachy.head.look_at(0.5, 0.3, 0, duration=0.5)
        time.sleep(0.1)
        reachy.head.look_at(0.5, -0.3, 0, duration=0.5)

        reachy.head.r_antenna.goal_position = -degree
        reachy.head.l_antenna.goal_position = 70-degree
        
   
    #back to default
    reachy.head.l_antenna.goal_position = 0.0
    reachy.head.r_antenna.goal_position = 0.0
    reachy.head.look_at(0.5, 0, 0, duration=0.5)
    time.sleep(1)

    reachy.turn_off_smoothly("head")
    
