import random

from ..Animations.Player import play_sound
from ..constants import NEXT_MOVE_HUMAN
from ..Helper.Safely import safely_run


def sentence_nextmove_hm():
    safely_run(
        play_sound(random.choice(NEXT_MOVE_HUMAN), True),
        "[Sentence next_move_hm] Sound konnte nicht abgespielt werden",
    )
