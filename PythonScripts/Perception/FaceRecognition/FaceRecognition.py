import recognition

class FaceRecognition:
    def __init__(self, reachy, move):
        self.reachy = reachy
        self.move = move

    def detect_human_player(self):
        recognition.detect_human_player(self.reachy, self.move)
    
    def look_at_human_player(self):
        recognition.look_at_human_player(self.reachy, self.move)
