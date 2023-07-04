from Perception.FaceRecognition import recognition

class FaceRecognition:
    def __init__(self):
        pass
    def identify_human_player(self, reachy, move):
        face_encoding = recognition.identify_human_player(reachy, move)
        recognition.serialize_player_face(face_encoding)
    
    def look_at_human_player(self, reachy, move):
        try:
            face_encoding = recognition.deserialize_player_face()
        except:
            print("No face saved. Starting recognition process...")
            face_encoding = recognition.identify_human_player(reachy, move)
        
        recognition.look_at_human_player(reachy, move, face_encoding)
