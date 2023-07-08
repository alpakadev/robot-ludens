import random 

from ..constants import WIN_PREVENT_FAILED
from ..Animations.Player import play_sound

def sentence_win_prevent_failed():

    play_sound(random.choice(WIN_PREVENT_FAILED), block = True)