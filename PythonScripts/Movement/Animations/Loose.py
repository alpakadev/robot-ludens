import time
from Sad import animation_sad


def animation_loose(reachy):
    reachy.head.look_at(0.05, 0, 0, duration=0.5)
    time.sleep(1.0)
    reachy.head.look_at(0.5, 0, -0.4, 0.5)
    time.sleep(1.5)
    reachy.head.l_antenna.speed_limit = 150.0
    reachy.head.r_antenna.speed_limit = 150.0
    reachy.head.l_antenna.goal_position = 140.0
    reachy.head.r_antenna.goal_position = -140.0
    time.sleep(2.0)
    reachy.head.look_at(0.05, -0.02, -0.04, duration=0.5)

    animation_sad(reachy)
