import time
#from ..MoveImpl import MoveImpl

def animation_lose(reachy): #with unity turn head more down when looking sideway sonst fertig
    reachy.turn_on("head")
    reachy.head.look_at(0.5, 0, 0, duration=0.5)

    time.sleep(1.0)

    reachy.head.look_at(0.5, 0, -0.4, 0.7)

    time.sleep(0.5)

    reachy.head.l_antenna.speed_limit = 90.0
    reachy.head.r_antenna.speed_limit = 90.0
    reachy.head.l_antenna.goal_position = 140.0
    reachy.head.r_antenna.goal_position = -140.0

    time.sleep(2.0)

    reachy.head.look_at(0.05, -0.03, -0.04, duration=0.7)
    time.sleep(3.0)

    #move_body(0.1,0)


    reachy.head.look_at(0.5, 0, 0.0, 1.0)
 
    reachy.head.l_antenna.goal_position = 0.0
    reachy.head.r_antenna.goal_position = 0.0
    time.sleep(1.0)
    reachy.turn_off("head")
