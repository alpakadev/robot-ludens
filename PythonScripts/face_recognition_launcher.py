import Perception.FaceRecognition.recognition as recognition
from reachy_sdk import ReachySDK
import reachy_sdk
import time
import asyncio
from Movement.MoveFacade import MoveFacade
reachy = ReachySDK("localhost")
"""move = MoveFacade()
move.set_dependencies(reachy, None, None)

# Das sollte eine Datei speichern mit einem erkannten Gesicht
# Falls kein Gesicht im Bild ist sollte er den Kopf einmal nach links und rechts drehen und nach einem Gesicht suchen
recognition.detect_human_player(reachy, move)

time.sleep(5)

# Nach dem ein Gesicht erkannt wurde soll er seinen Blick so ausrichten, dass er die Person anschaut
# Falls der Kopf sich gar nicht bewegt ist etwas schief gelaufen. Falls er sich komisch bewegt, dann sind in center_vision_on_face unten die Faktoren vertauscht
recognition.look_at_human_player(reachy, move)"""

face = recognition.detect_human_player(reachy)
recognition.look_at_human_player(reachy, face)