from playsound import playsound


def play_sound(sound, block):
    try:
        playsound("./"+sound, block)
        print("[Success] Sound was played", "./"+sound)
    except Exception as exception:
        print('[Failure] SoundFile "'+'./'+sound+'" Could not be played')
        print(exception)

#playsound("./PythonScripts/Movement/Sounds/chance_human/chance_hm2.wav")
