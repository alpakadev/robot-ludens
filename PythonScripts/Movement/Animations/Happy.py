import time
from reachy_sdk.trajectory import goto
from reachy_sdk.trajectory.interpolation import InterpolationMode


def animation_happy(reachy): #antennas and head tilted
    
    reachy.turn_on("head")

    reachy.head.l_antenna.speed_limit = 25.0
    reachy.head.r_antenna.speed_limit = 25.0
    reachy.head.l_antenna.goal_position = 40.0
    reachy.head.r_antenna.goal_position = -40.0

    time.sleep(0.5)
    reachy.head.l_antenna.speed_limit = 75.0
    reachy.head.r_antenna.speed_limit = 75.0
    for _ in range(2):
        
        head_tilt_r = {
            reachy.head.l_antenna: 70,
            reachy.head.r_antenna: -70,  
            reachy.head.neck_roll: -25,  # tilt +left to -right 35
            reachy.head.neck_pitch: -10,   # up down
            reachy.head.neck_yaw: 15,     # left to right side
            }

        goto(
            goal_positions=head_tilt_r,
            duration=0.8,
            interpolation_mode=InterpolationMode.MINIMUM_JERK
            )
        time.sleep(0.3)
        reachy.head.l_antenna.goal_position = 55.0
        reachy.head.r_antenna.goal_position = -55.0
        time.sleep(0.1)

        
        head_tilt_l = {
        reachy.head.l_antenna: 20,
        reachy.head.r_antenna: -20,  
        reachy.head.neck_roll: 25,  # tilt +left to -right 35
        reachy.head.neck_pitch: -10,   # up down
        reachy.head.neck_yaw: -15,     # left to right side
        }

        goto(
            goal_positions=head_tilt_l,
            duration=0.8,
            interpolation_mode=InterpolationMode.MINIMUM_JERK
            )
        time.sleep(0.5)

        
        
        

    reachy.head.look_at(0.5, -0, 0, duration=0.5)

    reachy.head.l_antenna.goal_position = 0.0
    time.sleep(0.1)
    reachy.head.r_antenna.goal_position = 0.0

