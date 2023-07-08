import random 

from ..constants import CHANCE_WIN_REACHY
from ..Animations.Player import play_sound

def sentence_chance_rh():

    play_sound(random.choice(CHANCE_WIN_REACHY), block = True)