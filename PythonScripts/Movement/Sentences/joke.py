import random

from ..Animations.Player import play_sound
from ..constants import JOKE
from ..Helper.Safely import safely_run


def sentence_joke():
    safely_run(
        play_sound(random.choice(JOKE), True),
        "[Sentence joke] Sound konnte nicht abgespielt werden",
    )
