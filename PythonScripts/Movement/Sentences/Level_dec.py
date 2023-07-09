import random

from ..constants import LEVEL_DECREASE
from ..Animations.Player import play_sound
from ..Helper.Safely import safely_run


def sentence_level_dec():
    safely_run(play_sound(random.choice(LEVEL_DECREASE), True),
               "[Sentence Level_dec] Sound konnte nicht abgespielt werden")
