from.Player import play_sound 

inhale =  "PythonScripts/Movement/Sounds/inhaling.mp3" 

#sound isnt played through reachy's speakers...fix needed
def animation_inhale():
    
    play_sound(inhale, block = True) 