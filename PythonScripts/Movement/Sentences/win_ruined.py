import random

from ..Animations.Player import play_sound
from ..constants import WIN_PREVENT_FAILED
from ..Helper.Safely import safely_run


def sentence_win_ruined():
    safely_run(
        play_sound(random.choice(WIN_PREVENT_FAILED), True),
        "[Sentence win_prevent_failed] Sound konnte nicht abgespielt werden",
    )
