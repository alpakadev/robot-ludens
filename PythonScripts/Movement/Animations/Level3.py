import time


def animation_level3(reachy):
    """
    indicating level3: expert
    """
    reachy.turn_on("head")

    reachy.head.l_antenna.goal_position = -85.0
    reachy.head.r_antenna.goal_position = 85.0
    time.sleep(2.5)

    reachy.head.l_antenna.goal_position = 0.0
    reachy.head.r_antenna.goal_position = 0.0
    # time.sleep(1.0)
