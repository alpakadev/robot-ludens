import time

from .. import constants


def animation_disapproval(reachy):
    reachy.head.look_at(constants.HEAD_LOOK_DOWN)

    time.sleep(0.5)

    reachy.head.l_antenna.speed_limit = 70.0
    reachy.head.r_antenna.speed_limit = 70.0
    reachy.head.l_antenna.goal_position = 50.0
    reachy.head.r_antenna.goal_position = -90.0

    reachy.head.look_at(constants.HEAD_LOOK_FRONT, duration=0.5)

    # Head shaking
    for i in range(3):
        reachy.head.look_at(0.5, 0.3, 0, duration=0.5)
        reachy.head.look_at(0.5, -0.3, 0, duration=0.5)

    reachy.head.l_antenna.goal_position = 0.0
    reachy.head.r_antenna.goal_position = 0.0
    reachy.head.look_at(constants.HEAD_LOOK_FRONT, duration=0.5)
