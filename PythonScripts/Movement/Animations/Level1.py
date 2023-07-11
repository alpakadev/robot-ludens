import time


def animation_level1(reachy):
    """
    indicating level 1: easy
    """
    reachy.turn_on("head")

    reachy.head.l_antenna.goal_position = 30.0
    reachy.head.r_antenna.goal_position = -30.0
    time.sleep(2.5)

    reachy.head.l_antenna.goal_position = 0.0
    reachy.head.r_antenna.goal_position = 0.0
    time.sleep(1.0)
