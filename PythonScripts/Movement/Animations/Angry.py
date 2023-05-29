import time


def animation_angry(reachy):
    """
    pushes cylinders and cubes of the board, antennas  at 45°
    """

    reachy.head.l_antenna.speed_limit = 90.0
    reachy.head.r_antenna.speed_limit = 90.0

    for _ in range(3):
        reachy.head.l_antenna.goal_position = -70.0
        reachy.head.r_antenna.goal_position = 70.0

        time.sleep(0.50)

        reachy.head.l_antenna.goal_position = -80.0
        reachy.head.r_antenna.goal_position = 80.0

    time.sleep(0.1)

    reachy.head.l_antenna.goal_position = 0.0
    reachy.head.r_antenna.goal_position = 0.0
