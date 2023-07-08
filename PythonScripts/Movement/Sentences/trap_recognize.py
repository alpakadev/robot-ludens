import random 

from ..constants import TRAP_RECOGNIZE
from ..Animations.Player import play_sound

def sentence_trap_recognize():

    play_sound(random.choice(TRAP_RECOGNIZE), block = True)