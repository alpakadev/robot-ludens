import random 

from ..constants import JOKE
from ..Animations.Player import play_sound

def sentence_joke():

    play_sound(random.choice(JOKE), block = True)