import random

from ..Animations.Player import play_sound
from ..constants import CHANCE_WIN_REACHY
from ..Helper.Safely import safely_run


def sentence_chance_rh():
    safely_run(
        play_sound(random.choice(CHANCE_WIN_REACHY), True),
        "[Sentence chance_rh] Sound konnte nicht abgespielt werden",
    )
