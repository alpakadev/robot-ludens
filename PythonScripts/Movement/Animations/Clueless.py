
import time

from reachy_sdk.trajectory import goto
from reachy_sdk.trajectory.interpolation import InterpolationMode

def animation_clueless(reachy): #not done yet tilt head right to left
    # with hanging antennas less sad than sad_antennas
    reachy.turn_on("head")
    reachy.head.l_antenna.speed_limit = 90.0
    reachy.head.r_antenna.speed_limit = 90.0

    reachy.head.l_antenna.goal_position = -35.0
    reachy.head.r_antenna.goal_position = 50.0
    time.sleep(1.0)

    for x in range(2):

        start_head = {
            reachy.head.l_antenna: -35,
            reachy.head.r_antenna: -65,  
            reachy.head.neck_roll: 15,  # tilt +left to -right 35
            reachy.head.neck_pitch: 10,   # up down
            reachy.head.neck_yaw: 15,     # left to right side
            }
    
        goto(
            goal_positions=start_head,
            duration=1.6,
            interpolation_mode=InterpolationMode.MINIMUM_JERK
            )

        head2 = {
            reachy.head.l_antenna: 55,
            reachy.head.r_antenna: 35,  
            reachy.head.neck_roll: -35,  # tilt +left to -right 35
            reachy.head.neck_pitch: 0,   # up down
            reachy.head.neck_yaw: -10,     # left to right side
            }
        goto(
            goal_positions=head2,
            duration=1.5,
            interpolation_mode=InterpolationMode.MINIMUM_JERK,
            )
        time.sleep(0.5)

      
    reachy.head.look_at(0.5, 0, 0, 1)
    reachy.head.l_antenna.goal_position = 0.0
    time.sleep(0.1)
    reachy.head.r_antenna.goal_position = 0.0