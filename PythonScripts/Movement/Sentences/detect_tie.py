import random 

from ..constants import DETECT_TIE
from ..Animations.Player import play_sound

def sentence_detect_tie():

    play_sound(random.choice(DETECT_TIE), block = True)