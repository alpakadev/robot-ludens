import random

from ..constants import WIN_PREVENT_FAILED
from ..Animations.Player import play_sound
from ..Helper.Safely import safely_run


def sentence_win_prevent_failed():
    safely_run(play_sound(random.choice(WIN_PREVENT_FAILED), True),
               "[Sentence win_prevent_failed] Sound konnte nicht abgespielt werden")
