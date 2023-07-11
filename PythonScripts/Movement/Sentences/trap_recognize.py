import random

from ..Animations.Player import play_sound
from ..constants import TRAP_RECOGNIZE
from ..Helper.Safely import safely_run


def sentence_trap_recognize():
    safely_run(play_sound(random.choice(TRAP_RECOGNIZE), True),
               "[Sentence trap_recognize] Sound konnte nicht abgespielt werden")
