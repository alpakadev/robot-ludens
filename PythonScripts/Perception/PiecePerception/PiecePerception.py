from PiecePerception.unused_pieces_detection import unused_pieces_detection
from PiecePerception.nearest_unused_piece import get_nearest_unused_piece

class PiecePerception:
    def __init__(self, config):
        self.config = config
    
    def get_unused_pieces_from_frame(self, frame):
        return unused_pieces_detection(frame)
    
    def get_nearest_unused_piece(self, piece_coordinates):
        return get_nearest_unused_piece(piece_coordinates)