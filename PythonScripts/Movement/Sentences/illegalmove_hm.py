import random 

from ..constants import ILLEGALMOVE_HUMAN
from ..Animations.Player import play_sound

def sentence_illegalmove_hm():

    play_sound(random.choice(ILLEGALMOVE_HUMAN), block = True)