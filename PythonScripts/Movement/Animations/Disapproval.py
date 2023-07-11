import random
import time

from ..constants import CHANCE_WIN_HUMAN, CHANCE_WIN_REACHY
from ..Helper.Safely import safely_run
from .Player import play_sound


def animation_disapproval(reachy, use_sound):
    """
    head shaking with changing antennas 
    """
    reachy.turn_on("head")
    reachy.head.look_at(0.05, 0, -0.03, 1.0)
    time.sleep(0.5)

    reachy.head.r_antenna.speed_limit = 90.0
    reachy.head.l_antenna.speed_limit = 90.0

    reachy.head.r_antenna.goal_position = -45.0
    reachy.head.l_antenna.goal_position = 65.0
    time.sleep(1.5)

    reachy.head.look_at(0.05, 0, 0, duration=0.5, )

    p = random.random()
    if p < 0.5:
        safely_run(play_sound(random.choice(CHANCE_WIN_HUMAN), False),
                   "[Anim Disapproval] Sound konnte nicht abgespielt werden") if use_sound else None
    else:
        safely_run(play_sound(random.choice(CHANCE_WIN_REACHY), False),
                   "[Anim Clueless] Sound konnte nicht abgespielt werden") if use_sound else None

    # Head shaking
    for i in range(3):
        degree = random.randint(50, 80)  # randomized degree for antennas

        reachy.head.l_antenna.speed_limit = 40.0
        reachy.head.r_antenna.speed_limit = 40.0

        reachy.head.look_at(0.5, 0.3, 0, duration=0.5)
        time.sleep(0.1)
        reachy.head.look_at(0.5, -0.3, 0, duration=0.5)

        reachy.head.r_antenna.goal_position = -degree
        reachy.head.l_antenna.goal_position = 70 - degree

    # back to default
    reachy.head.l_antenna.goal_position = 0.0
    reachy.head.r_antenna.goal_position = 0.0
    reachy.head.look_at(0.5, 0, 0, duration=0.5)
    time.sleep(1)

    reachy.turn_off_smoothly("head")
