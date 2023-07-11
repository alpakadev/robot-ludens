import random

from ..Animations.Player import play_sound
from ..constants import TRAP_DONE
from ..Helper.Safely import safely_run


def sentence_trap_done():
    safely_run(
        play_sound(random.choice(TRAP_DONE), True),
        "[Sentence trap_done] Sound konnte nicht abgespielt werden",
    )
