import random

from ..constants import CHANCE_WIN_HUMAN
from ..Animations.Player import play_sound
from ..Helper.Safely import safely_run


def sentence_chance_hm():
    safely_run(play_sound(random.choice(CHANCE_WIN_HUMAN), True),
               "[Sentence chance_hm] Sound konnte nicht abgespielt werden")
