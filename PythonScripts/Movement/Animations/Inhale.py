from.Player import play_sound # pip install playsound

# TODO Should not be a Global variable
inhale =  "./PythonScripts/Movement/Sounds/inhaling.mp3"

# sound isnt played through reachy's speakers...~fix needed~
# fix: Project needs to be run on Reachy.
# Playsound does not send the Soundfiles to reachy
def animation_inhale():
    
    play_sound(inhale, block = True) 