import time
import random


def animation_disapproval(reachy): #fertig
    reachy.turn_on("head")
    reachy.head.look_at(0.5, 0.0, -0.4, 1.0)  #looking down 

    time.sleep(0.5)
    reachy.head.l_antenna.speed_limit = 90.0
    reachy.head.r_antenna.speed_limit = 90.0
    reachy.head.l_antenna.goal_position = 40.0
    reachy.head.r_antenna.goal_position = -80.0
    time.sleep(1.5)
    reachy.head.look_at(0.05, 0, 0, duration=0.5,)

    # Head shaking
    degree = random.randint(15,30) #

    for i in range(3):
        degree += random.randint(10,30) #
        reachy.head.l_antenna.speed_limit = 40.0
        reachy.head.r_antenna.speed_limit = 40.0
        
        reachy.head.look_at(0.5, 0.3, 0, duration=0.5)
        time.sleep(0.1)
        reachy.head.look_at(0.5, -0.3, 0, duration=0.5)
        
        reachy.head.l_antenna.goal_position = degree #
        print(reachy.head.l_antenna.goal_position)
        reachy.head.r_antenna.goal_position = (40-degree) #
        print(reachy.head.r_antenna.goal_position)
    
        

        
    #back to default
    reachy.head.l_antenna.goal_position = 0.0
    reachy.head.r_antenna.goal_position = 0.0
    reachy.head.look_at(0.05, 0, 0, duration=0.5)
    
