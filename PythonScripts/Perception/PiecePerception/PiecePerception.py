from .nearest_unused_piece import get_nearest_unused_piece
from .game_figure_detection import get_all_pieces_coordinates
from .estimate_metric_distance import estimate_metric_distance

class PiecePerception:
    def __init__(self, config):
        self.config = config
    
    def do_get_nearest_unused_piece(self, frame, board_corners):
        return get_nearest_unused_piece(frame, board_corners)

    def do_get_all_pieces_coordinates(self, frame, board_corners, 
                                      game_board_coords):
        return get_all_pieces_coordinates(frame, board_corners, 
                                          game_board_coords)
    
    def do_estimate_metric_distance(self, frame, board_corners, 
                                    centroid_x, centroid_y):
        return estimate_metric_distance(frame, board_corners, 
                                        centroid_x, centroid_y)
