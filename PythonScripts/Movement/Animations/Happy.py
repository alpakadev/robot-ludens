import time

from reachy_sdk.trajectory import goto
from reachy_sdk.trajectory.interpolation import InterpolationMode


def animation_happy(reachy):
    """
    alternative for happy_antennas;  head swinging side to side
    """
    reachy.turn_on("head")

    reachy.head.l_antenna.speed_limit = 25.0
    reachy.head.r_antenna.speed_limit = 25.0

    reachy.head.l_antenna.goal_position = 30.0
    reachy.head.r_antenna.goal_position = -30.0
    time.sleep(0.5)

    reachy.head.l_antenna.speed_limit = 75.0
    reachy.head.r_antenna.speed_limit = 75.0

    for _ in range(4):
        
        head_tilt_r = {
            reachy.head.l_antenna: 70,
            reachy.head.r_antenna: -70,  
            reachy.head.neck_roll: 25,  # tilt +left to -right 35
            reachy.head.neck_pitch: 30,   # up down
            reachy.head.neck_yaw: 10,     # left to right side
        }

        goto(
            goal_positions=head_tilt_r,
            duration=0.45,
            interpolation_mode=InterpolationMode.MINIMUM_JERK
        )
        time.sleep(0.3)

        reachy.head.l_antenna.goal_position = 55.0
        reachy.head.r_antenna.goal_position = -55.0
        time.sleep(0.1)

        head_tilt_l = {
            reachy.head.l_antenna: 20,
            reachy.head.r_antenna: -20,  
            reachy.head.neck_roll: -5,  # tilt +left to -right 35
            reachy.head.neck_pitch: -25,   # up down
            reachy.head.neck_yaw: 10,     # left to right side
        }

        goto(
            goal_positions=head_tilt_l,
            duration=0.45,
            interpolation_mode=InterpolationMode.MINIMUM_JERK
        )
        time.sleep(0.5)

    #back to default
    reachy.head.look_at(0.5, 0, 0, duration=0.5)
    reachy.head.l_antenna.goal_position = 0.0
    reachy.head.r_antenna.goal_position = 0.0
    time.sleep(1)

    reachy.turn_off_smoothly("head")

