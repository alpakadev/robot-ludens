import random 

from ..constants import WAITING
from ..Animations.Player import play_sound

def sentence_waiting():

    play_sound(random.choice(WAITING), block = True)