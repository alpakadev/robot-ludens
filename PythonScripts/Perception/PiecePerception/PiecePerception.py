from .unused_pieces_detection import unused_pieces_detection
from .nearest_unused_piece import get_nearest_unused_piece

class PiecePerception:
    def __init__(self, config):
        self.config = config
    
    def get_unused_pieces_from_frame(self, frame):
        return unused_pieces_detection(frame)
    
    def get_nearest_unused_piece(self, frame, board_corners):
        return get_nearest_unused_piece(frame, board_corners)