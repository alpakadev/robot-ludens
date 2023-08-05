import random
import time

from ..constants import LOSING
from ..Helper.Safely import safely_run
from .Player import play_sound


def animation_lose(reachy, use_sound):
    """
    looking down-sideways with sad antennas
    """
    reachy.turn_on("head")

    reachy.head.look_at(0.5, 0, 0, duration=0.5)
    time.sleep(1.0)

    reachy.head.look_at(0.05, 0, -0.05, 0.7)
    time.sleep(0.5)

    safely_run(
        play_sound(random.choice(LOSING), False),
        "[Anim Losing] Sound konnte nicht abgespielt werden",
    ) if use_sound else None

    reachy.head.l_antenna.speed_limit = 90.0
    reachy.head.r_antenna.speed_limit = 90.0
    reachy.head.l_antenna.goal_position = 140.0
    reachy.head.r_antenna.goal_position = -140.0
    time.sleep(1.0)

    reachy.head.look_at(0.05, -0.03, -0.04, duration=0.7)
    time.sleep(1.5)

    # back to default
    reachy.head.look_at(0.5, 0, 0.0, 1.0)
    reachy.head.l_antenna.goal_position = 0.0
    reachy.head.r_antenna.goal_position = 0.0
    # time.sleep(1.0)

    reachy.turn_off_smoothly("head")
