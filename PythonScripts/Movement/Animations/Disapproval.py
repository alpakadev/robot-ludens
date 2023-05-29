import time


def animation_disapproval(reachy):
    reachy.head.look_at(0.5, 0, -0.4, 1.0)  # at board

    time.sleep(0.5)

    reachy.head.l_antenna.speed_limit = 20.0
    reachy.head.r_antenna.speed_limit = 20.0
    reachy.head.l_antenna.goal_position = 50.0
    reachy.head.r_antenna.goal_position = -90.0
    reachy.head.look_at(0.05, 0, 0, duration=0.5)  # default

    for i in range(3):  # shakes head
        reachy.head.look_at(0.5, 0.3, 0, duration=0.5)
        reachy.head.look_at(0.5, -0.3, 0, duration=0.5)

    reachy.head.l_antenna.goal_position = 0.0  # default antennas
    reachy.head.r_antenna.goal_position = 0.0
    reachy.head.look_at(0.05, 0, 0, duration=0.5)  # goes back to default position
