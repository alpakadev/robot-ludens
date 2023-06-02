import time



def animation_disapproval(reachy):
   
    reachy.head.look_at(0.5, 0.0, -0.4, 1.0)  

    time.sleep(0.5)
    reachy.head.l_antenna.speed_limit = 50.0
    reachy.head.r_antenna.speed_limit = 50.0
    reachy.head.l_antenna.goal_position = 60.0
    reachy.head.r_antenna.goal_position = -90.0

    reachy.head.look_at(0.05, 0, 0, duration=0.5,)

    # Head shaking
    for i in range(3):
        reachy.head.look_at(0.5, 0.3, 0, duration=0.5)
        reachy.head.look_at(0.5, -0.3, 0, duration=0.5)
        
    #back to default
    reachy.head.l_antenna.goal_position = 0.0
    reachy.head.r_antenna.goal_position = 0.0
    reachy.head.look_at(0.05, 0, 0, duration=0.5)
