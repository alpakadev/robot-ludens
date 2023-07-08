import random 

from ..constants import CHANCE_WIN_HUMAN
from ..Animations.Player import play_sound

def sentence_chance_hm():

    play_sound(random.choice(CHANCE_WIN_HUMAN), block = True)