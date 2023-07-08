import random 

from ..constants import LEVEL_INCREASE
from ..Animations.Player import play_sound

def sentence_level_inc():

    play_sound(random.choice(LEVEL_INCREASE), block = True)

