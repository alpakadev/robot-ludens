import random 

from ..constants import WIN_PREVENT
from ..Animations.Player import play_sound

def sentence_win_prevent():

    play_sound(random.choice(WIN_PREVENT), block = True)