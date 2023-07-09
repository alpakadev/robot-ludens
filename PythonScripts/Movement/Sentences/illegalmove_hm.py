import random

from ..constants import ILLEGALMOVE_HUMAN
from ..Animations.Player import play_sound
from ..Helper.Safely import safely_run


def sentence_illegalmove_hm():
    safely_run(play_sound(random.choice(ILLEGALMOVE_HUMAN), True),
               "[Sentence illegalmove_hm] Sound konnte nicht abgespielt werden")
