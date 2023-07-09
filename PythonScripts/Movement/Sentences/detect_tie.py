import random

from ..constants import DETECT_TIE
from ..Animations.Player import play_sound
from ..Helper.Safely import safely_run


def sentence_detect_tie():
    safely_run(play_sound(random.choice(DETECT_TIE), True),
               "[Sentence detect_tie] Sound konnte nicht abgespielt werden")
