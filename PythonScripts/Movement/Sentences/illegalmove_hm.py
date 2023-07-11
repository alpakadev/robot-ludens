import random

from ..Animations.Player import play_sound
from ..constants import ILLEGALMOVE_HUMAN
from ..Helper.Safely import safely_run


def sentence_illegalmove_hm():
    safely_run(play_sound(random.choice(ILLEGALMOVE_HUMAN), True),
               "[Sentence illegalmove_hm] Sound konnte nicht abgespielt werden")
