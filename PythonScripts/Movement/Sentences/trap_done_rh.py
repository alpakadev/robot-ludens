import random 

from ..constants import TRAP_DONE
from ..Animations.Player import play_sound

def sentence_trap_done():

    play_sound(random.choice(TRAP_DONE), block = True)