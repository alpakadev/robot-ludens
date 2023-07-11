import random

from ..Animations.Player import play_sound
from ..constants import LEVEL_DECREASE
from ..Helper.Safely import safely_run


def sentence_level_dec():
    safely_run(play_sound(random.choice(LEVEL_DECREASE), True),
               "[Sentence Level_dec] Sound konnte nicht abgespielt werden")
