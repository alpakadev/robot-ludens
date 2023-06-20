import recognition
import reachy_sdk
import Movement.MoveFacade

reachy = ReachySDK("192.168.3.94")
move = MoveFacade()


recognition.detect_human_player(reachy, move)()