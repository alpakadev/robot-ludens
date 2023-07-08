import random 

from ..constants import ILLEGALMOVE_REACHY
from ..Animations.Player import play_sound

def sentence_illegalmove_rh():

    play_sound(random.choice(ILLEGALMOVE_REACHY), block = True)