import time


def animation_sad_antennas(reachy):
    reachy.head.l_antenna.speed_limit = 90.0
    reachy.head.r_antenna.speed_limit = 90.0

    reachy.head.l_antenna.goal_position = 140.0
    reachy.head.r_antenna.goal_position = -140.0

    time.sleep(5.0)

    reachy.head.l_antenna.goal_position = 0.0
    reachy.head.r_antenna.goal_position = 0.0