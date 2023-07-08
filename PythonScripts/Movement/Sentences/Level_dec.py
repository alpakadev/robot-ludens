import random 

from ..constants import LEVEL_DECREASE
from ..Animations.Player import play_sound

def sentence_level_dec():

    play_sound(random.choice(LEVEL_DECREASE), block = True)
