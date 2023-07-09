import random

from ..constants import NEXT_MOVE_REACHY
from ..Animations.Player import play_sound
from ..Helper.Safely import safely_run


def sentence_nextmove_rh():
    safely_run(play_sound(random.choice(NEXT_MOVE_REACHY), True),
               "[Sentence next_move_rh] Sound konnte nicht abgespielt werden")
