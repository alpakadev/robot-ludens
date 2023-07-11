from .board_cases_detection import calc_board_cases
from .game_board_detection import game_board_detection
from .image_stability import get_stable_image

class BoardPerception:
    def __init__(self, reachy, config):
        self.config = config
        self.reachy = reachy
        
    
    def do_get_board_corners(self, frame):
        # Determine corner points of the board
        board_coordinates = game_board_detection(frame, self.config)
        if len(board_coordinates) < 4:
            raise IndexError("Less than four board corners identified")
        else:
            return board_coordinates
    
    def do_get_board_cases(self, board_corner_coordinates):
        # Determine all other corner points of all squares
        # Takes board corners as given
        board_cases_coordinates = calc_board_cases(
                                      board_corner_coordinates, 
                                      self.config)
        return board_cases_coordinates
    
    def do_get_stable_board_image(self):
        return get_stable_image(self.reachy, self.config)