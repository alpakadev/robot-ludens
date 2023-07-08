HOST_ADDRESS = '192.168.1.94'

ORIGIN_COORDINATES = [0.15, -0.31, -0.38]

GRIP_FORCE_HOLDING = 50
GRIP_FORCE_HOLDING_THRESHOLD = 100

# The distance to position hand in front of object
DELTA_FRONT = 0.07
# The distance above the object to move the arm back
DELTA_HEIGHT = 0.22
#Distance about all cylinders on the field
DELTA_SAFE_HEIGHT = 0.03
# The distance from the middle of the hand to non-moving part
DELTA_HAND_WIDTH = 0.02
# The distance form the middle to tip of the hand
DELTA_HAND_TIP = 0.01

POS_ARM_AT_RIGHT_ANGLE = [0.36, -0.20, -0.28]
POS_SAVE_COORDINATES = [0.36, -0.2, 0]
POS_ARM_SIDE = [0, -0.45, -0.2]

HEAD_LOOK_FRONT = [0.5, 0, 0]
HEAD_LOOK_DOWN = [0.05, 0, -0.05]

GRIPPER_OPEN_FULL = -40
GRIPPER_CLOSED = 5

#sounds

ANGRY_SOUND =  ["PythonScripts/Movement/Sounds/angry/gedult erschöpft.m4a","PythonScripts/Movement/Sounds/angry/so gehts nicht weiter.m4a" ]
CHANCE_WIN_HUMAN = ["PythonScripts/Movement/Sounds/chance_human/404.m4a", "PythonScripts/Movement/Sounds/chance_human/fallenkarte.m4a",
                  "PythonScripts/Movement/Sounds/chance_human/ich sehe was.m4a", "PythonScripts/Movement/Sounds/chance_human/ups.m4a"]
CHANCE_WIN_REACHY = ["PythonScripts/Movement/Sounds/chance_reachy/jetzt ist es aus.m4a", "PythonScripts/Movement/Sounds/chance_reachy/sieg in sichtweite.m4a",
                   "PythonScripts/Movement/Sounds/chance_reachy/so geht es zuende.m4a"]
BEFORE_THINKING = ["PythonScripts/Movement/Sounds/before_thinking/ich muss überlegen.mp3", "PythonScripts/Movement/Sounds/before_thinking/lass mich denken.mp3"]
DETECT_TIE = ["PythonScripts/Movement/Sounds/detect_tie/ein unentschieden liegt inder luft.m4a", "PythonScripts/Movement/Sounds/detect_tie/ich erkenne eine packsituation.m4a", 
              "PythonScripts/Movement/Sounds/detect_tie/ich sehe schon worauf.mp3", "PythonScripts/Movement/Sounds/detect_tie/meine daten lassen....m4a",
              "PythonScripts/Movement/Sounds/detect_tie/spiel wird in ein unentschieden enden.m4a", "PythonScripts/Movement/Sounds/detect_tie/unentschieden in der Luft.m4a",
              "PythonScripts/Movement/Sounds/detect_tie/unentschieden ist unausweichlich.m4a", "PythonScripts/Movement/Sounds/detect_tie/wir uns auf ein untendschieden.m4a"]
START_HUMAN = ["PythonScripts/Movement/Sounds/game_start_human/du beginnst.mp3", "PythonScripts/Movement/Sounds/game_start_human/du bist an der reihe.mp3", "PythonScripts/Movement/Sounds/game_start_human/du bist an der reihe.mp3",
                "PythonScripts/Movement/Sounds/game_start_human/du bist an der reihe.mp3", "PythonScripts/Movement/Sounds/game_start_human/du darfst beginnen.mp3", "PythonScripts/Movement/Sounds/game_start_human/du eröffnest das match.mp3",
                "PythonScripts/Movement/Sounds/game_start_human/du fängst an.mp3", "PythonScripts/Movement/Sounds/game_start_human/du setzt den ersten stein.mp3", "PythonScripts/Movement/Sounds/game_start_human/fang an.mp3"]
START_REACHY = ["PythonScripts/Movement/Sounds/game_start_reachy/ich beginne.mp3", "PythonScripts/Movement/Sounds/game_start_reachy/ich bin an der reihe.mp3",
               "PythonScripts/Movement/Sounds/game_start_reachy/ich bin der startspieler.mp3", "PythonScripts/Movement/Sounds/game_start_reachy/ich eröffnne das match.mp3",
               "PythonScripts/Movement/Sounds/game_start_reachy/ich eröffnne das match.mp3", "PythonScripts/Movement/Sounds/game_start_reachy/ich setzte ersten stein.mp3",
               "PythonScripts/Movement/Sounds/game_start_reachy/ich werde anfangen.mp3", "PythonScripts/Movement/Sounds/game_start_reachy/ich werde beginnen.mp3"]
ILLEGALMOVE_REACHY = ["PythonScripts/Movement/Sounds/illegalmove_human/das darf so nicht stehen belieben.mp3", "PythonScripts/Movement/Sounds/illegalmove_human/das ist ein illegaler zug.mp3",
                      "PythonScripts/Movement/Sounds/illegalmove_human/halt stopp.mp3", "PythonScripts/Movement/Sounds/illegalmove_human/so geht das aber nicht.mp3"]
ILLEGALMOVE_HUMAN = ["PythonScripts/Movement/Sounds/illegalmove_reachy/ich mache zug.m4a", "PythonScripts/Movement/Sounds/illegalmove_reachy/regelkonform.m4a", "PythonScripts/Movement/Sounds/illegalmove_reachy/schmetterling.m4a", "PythonScripts/Movement/Sounds/illegalmove_reachy/total richtig.m4a",
                     "PythonScripts/Movement/Sounds/illegalmove_reachy/völlig legal.m4a"]
JOKE = ["PythonScripts/Movement/Sounds/joke/Wie viele Informatik.m4a"]
LEVEL_DECREASE = ["PythonScripts/Movement/Sounds/level_decrease/ohne mühe.mp3", "PythonScripts/Movement/Sounds/level_decrease/ohne mühe.mp3",
                  "PythonScripts/Movement/Sounds/level_decrease/sieht so aus dass ich mich zurücklegen kann.mp3", "PythonScripts/Movement/Sounds/level_decrease/streng dich mehr an.mp3"]
LEVEL_INCREASE = ["PythonScripts/Movement/Sounds/level_increase/ich gebe mir nun extra viel mühe.mp3", "PythonScripts/Movement/Sounds/level_increase/ich muss mich doch mehr anstrengen.mp3",
                  "PythonScripts/Movement/Sounds/level_increase/jz strenge ich mich mehr an.mp3"]
LOSING = ["PythonScripts/Movement/Sounds/losing/der sieg ist dein.m4a", "PythonScripts/Movement/Sounds/losing/du bist unschlagbar.m4a", "PythonScripts/Movement/Sounds/losing/du hast gewonnen.m4a", 
          "PythonScripts/Movement/Sounds/losing/glückwunsch.m4a", "PythonScripts/Movement/Sounds/losing/gut gespielt.m4a", "PythonScripts/Movement/Sounds/losing/starke leistung.m4a"]
NEXT_MOVE_HUMAN = ["PythonScripts/Movement/Sounds/next_move_human/dein zug.m4a", "PythonScripts/Movement/Sounds/next_move_human/du bist dran.m4a", "PythonScripts/Movement/Sounds/next_move_human/jetzt du.m4a"]
NEXT_MOVE_REACHY = ["PythonScripts/Movement/Sounds/next_move_reachy/berechnete logik.m4a", "PythonScripts/Movement/Sounds/next_move_reachy/hier komme ich.m4a", "PythonScripts/Movement/Sounds/next_move_reachy/jetzt bin ich dran.m4a",
                    "PythonScripts/Movement/Sounds/next_move_reachy/ich antworte mit diesem zug.m4a", "PythonScripts/Movement/Sounds/next_move_reachy/lass mich zeigen.m4a", "PythonScripts/Movement/Sounds/next_move_reachy/mein algorithmus.m4a",
                    "PythonScripts/Movement/Sounds/next_move_reachy/mit präzision.m4a", "PythonScripts/Movement/Sounds/next_move_reachy/pläne durchkreuzen.m4a", "PythonScripts/Movement/Sounds/next_move_reachy/überraschen.m4a"]
THINKING = ["PythonScripts/Movement/Sounds/thinking/was ist nächster zug.mp3", "PythonScripts/Movement/Sounds/thinking/was mache ich jz.mp3"]
TIE = ["PythonScripts/Movement/Sounds/tie/auf augenhöhe.m4a", "PythonScripts/Movement/Sounds/tie/bestes gegeben.m4a", "PythonScripts/Movement/Sounds/tie/es ist unentschieden.m4a", "PythonScripts/Movement/Sounds/tie/würdiger gegner.m4a"]
TRAP_DONE = ["PythonScripts/Movement/Sounds/trap_done_by_reachy/du sitzt in der falle.mp3", "PythonScripts/Movement/Sounds/trap_done_by_reachy/es gibt kein entkommen.mp3", "PythonScripts/Movement/Sounds/trap_done_by_reachy/es gibt keinen ausweg.mp3",
             "PythonScripts/Movement/Sounds/trap_done_by_reachy/ich bin noch nicht fertig mit dem gewinnen.mp3", "PythonScripts/Movement/Sounds/trap_done_by_reachy/jz hab ich dich.mp3"]
TRAP_RECOGNIZE = ["PythonScripts/Movement/Sounds/trap_recognize/das funktioniert bei mir nicht.m4a", "PythonScripts/Movement/Sounds/trap_recognize/ich durchschau dich.m4a", "PythonScripts/Movement/Sounds/trap_recognize/ich durchschaue deine strategie.m4a",
                  "PythonScripts/Movement/Sounds/trap_recognize/ich sehe was du versuchst.m4a"]

WIN_PREVENT = ["PythonScripts/Movement/Sounds/win_prevent/das muss ich verhindern.mp3", "PythonScripts/Movement/Sounds/win_prevent/das werde ich verhindern.mp3", "PythonScripts/Movement/Sounds/win_prevent/ich werde dich aufhalten.mp3",
               "PythonScripts/Movement/Sounds/win_prevent/keine chance.mp3", "PythonScripts/Movement/Sounds/win_prevent/nicht mit mir.mp3", "PythonScripts/Movement/Sounds/win_prevent/nicht mit mir.mp3", "PythonScripts/Movement/Sounds/win_prevent/siegchance.mp3"]
WIN_PREVENT_FAILED = ["PythonScripts/Movement/Sounds/win_prevent_failed/das kann nicht.m4a", "PythonScripts/Movement/Sounds/win_prevent_failed/ich wollte doch gewinnen.m4a", "PythonScripts/Movement/Sounds/win_prevent_failed/nicht aufgepasst.m4a", "PythonScripts/Movement/Sounds/win_prevent_failed/von dir lernen.m4a",
                      "PythonScripts/Movement/Sounds/win_prevent_failed/wie hast du gemacht.m4a"]
WINNING = ["PythonScripts/Movement/Sounds/winning/der sieg geht an mich.m4a", "PythonScripts/Movement/Sounds/winning/du hast verloren.m4a", "PythonScripts/Movement/Sounds/winning/ich bin ein gewinner.m4a", "PythonScripts/Movement/Sounds/winning/ich bin unschlagbar.m4a", 
           "PythonScripts/Movement/Sounds/winning/ich habe gewonnen.m4a", "PythonScripts/Movement/Sounds/winning/zeuge der kollision.m4a"]



WAITING =  ["PythonScripts/Movement/Sounds/waiting/Angst potter.wav","PythonScripts/Movement/Sounds/waiting/whistling.wav", "PythonScripts/Movement/Sounds/waiting/wer wird wohl gewinnen.wav",
            "PythonScripts/Movement/Sounds/waiting/nimm dir zeit zum nachdenken.wav", "PythonScripts/Movement/Sounds/waiting/na los ich warte.wav",
            "PythonScripts/Movement/Sounds/waiting/die spannung steigt.wav", "PythonScripts/Movement/Sounds/waiting/denk gut nach.wav",
            "PythonScripts/Movement/Sounds/waiting/bedenke deine schritte genau.wav", "PythonScripts/Movement/Sounds/waiting/Angst potter.wav"]