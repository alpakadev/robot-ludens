import time

from reachy_sdk.trajectory import goto
from reachy_sdk.trajectory.interpolation import InterpolationMode


def animation_clueless(reachy):
    """
    head tilted left to right with leaning antennas in same direction
    
    """
    reachy.turn_on("head")
    reachy.head.l_antenna.speed_limit = 90.0
    reachy.head.r_antenna.speed_limit = 90.0

    reachy.head.l_antenna.goal_position = -35.0
    reachy.head.r_antenna.goal_position = 50.0
    time.sleep(1.0)


    for _ in range(2):
        head_tilt_l = {
            reachy.head.l_antenna: -35,
            reachy.head.r_antenna: -65,
            reachy.head.neck_roll: 15,
            reachy.head.neck_pitch: 10,
            reachy.head.neck_yaw: 15,
        }

        goto(
            goal_positions=head_tilt_l,
            duration=1.6,
            interpolation_mode=InterpolationMode.MINIMUM_JERK
        )

        head_tilt_r = {
            reachy.head.l_antenna: 55,
            reachy.head.r_antenna: 35,
            reachy.head.neck_roll: -35,
            reachy.head.neck_pitch: 0,
            reachy.head.neck_yaw: -10,
        }

        goto(
            goal_positions=head_tilt_r,
            duration=1.5,
            interpolation_mode=InterpolationMode.MINIMUM_JERK,
        )
        time.sleep(0.5)

    # back to default
    reachy.head.look_at(0.5, 0, 0, 1)
    reachy.head.l_antenna.goal_position = 0.0
    reachy.head.r_antenna.goal_position = 0.0
    time.sleep(1)

    reachy.turn_off_smoothly("head")
