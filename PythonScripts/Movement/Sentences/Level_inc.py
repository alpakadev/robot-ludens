import random

from ..constants import LEVEL_INCREASE
from ..Animations.Player import play_sound
from ..Helper.Safely import safely_run


def sentence_level_inc():
    safely_run(play_sound(random.choice(LEVEL_INCREASE), True),
               "[Sentence Level_inc] Sound konnte nicht abgespielt werden")
