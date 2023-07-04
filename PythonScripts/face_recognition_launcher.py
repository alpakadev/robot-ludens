import Perception.FaceRecognition.recognition as recognition
import reachy_sdk
import time
import asyncio
from Movement.MoveFacade import MoveFacade
from Perception.PerceptionFacade import PerceptionFacade
#reachy = reachy_sdk.ReachySDK("192.168.1.94")

reachy = reachy_sdk.ReachySDK("localhost")
perc = PerceptionFacade()
move = MoveFacade()
move.set_dependencies(reachy, perc, None)
perc.set_dependencies(reachy, move, None)

perc.identify_human_player()
perc.look_at_human_player()

"""move = MoveFacade()
move.set_dependencies(reachy, None, None)

# Das sollte eine Datei speichern mit einem erkannten Gesicht
# Falls kein Gesicht im Bild ist sollte er den Kopf einmal nach links und rechts drehen und nach einem Gesicht suchen
recognition.detect_human_player(reachy, move)

time.sleep(5)

# Nach dem ein Gesicht erkannt wurde soll er seinen Blick so ausrichten, dass er die Person anschaut
# Falls der Kopf sich gar nicht bewegt ist etwas schief gelaufen. Falls er sich komisch bewegt, dann sind in center_vision_on_face unten die Faktoren vertauscht
recognition.look_at_human_player(reachy, move)"""

"""reachy.turn_on("head")
face = recognition.detect_human_player(reachy)
print(face)
time.sleep(5.0)
recognition.look_at_human_player(reachy, face)
reachy.turn_off_smoothly("head")"""