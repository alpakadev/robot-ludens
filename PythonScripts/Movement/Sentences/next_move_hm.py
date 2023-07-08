import random 

from ..constants import NEXT_MOVE_HUMAN
from ..Animations.Player import play_sound

def sentence_nextmove_hm():

    play_sound(random.choice(NEXT_MOVE_HUMAN), block = True)