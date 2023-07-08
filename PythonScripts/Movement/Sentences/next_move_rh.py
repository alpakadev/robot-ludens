import random 

from ..constants import NEXT_MOVE_REACHY
from ..Animations.Player import play_sound

def sentence_nextmove_rh():

    play_sound(random.choice(NEXT_MOVE_REACHY), block = True)