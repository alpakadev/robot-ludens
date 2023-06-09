from Perception.FaceRecognition import recognition

class FaceRecognition:
    def __init__(self):
        pass

    
    def do_identify_human_player(self, reachy, move):
        # Identifies the human player at the start of the game
        face_encoding = recognition.identify_human_player(reachy, move)
        recognition.serialize_player_face(face_encoding)
    
    def do_look_at_human_player(self, reachy, move):
        # move head to look at the human player that was identified
        try:
            face_encoding = recognition.deserialize_player_face()
        except FileNotFoundError:
            print("No face saved. Starting recognition process...")
            face_encoding = recognition.identify_human_player(reachy, move)
        
        recognition.look_at_human_player(reachy, move, face_encoding)
