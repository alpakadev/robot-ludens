import random

from ..constants import WIN_PREVENT
from ..Animations.Player import play_sound
from ..Helper.Safely import safely_run


def sentence_win_prevent():
    safely_run(play_sound(random.choice(WIN_PREVENT), True),
               "[Sentence win_prevent] Sound konnte nicht abgespielt werden")
