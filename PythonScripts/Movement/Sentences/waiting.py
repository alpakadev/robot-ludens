import random

from ..Animations.Player import play_sound
from ..constants import WAITING
from ..Helper.Safely import safely_run


def sentence_waiting():
    safely_run(
        play_sound(random.choice(WAITING), True),
        "[Sentence waiting] Sound konnte nicht abgespielt werden",
    )
