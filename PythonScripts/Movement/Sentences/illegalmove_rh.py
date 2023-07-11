import random

from ..Animations.Player import play_sound
from ..constants import ILLEGALMOVE_REACHY
from ..Helper.Safely import safely_run


def sentence_illegalmove_rh():
    safely_run(
        play_sound(random.choice(ILLEGALMOVE_REACHY), True),
        "[Sentence illegalmove_rh] Sound konnte nicht abgespielt werden",
    )
