from ..Exceptions.Exceptions import ViewCloudedError
from .board_cases_detection import get_board_cases
from .case_to_realworld_coordinates import case_to_realworld_coordinates
from .game_board_detection import game_board_detection
from .image_stability import get_stable_image

class BoardPerception:
    def __init__(self, reachy, config):
        self.config = config
        self.reachy = reachy
    
    def get_board_corners(self, frame):
        board_coordinates = game_board_detection(frame, self.config)
        if len(board_coordinates) < 4:
            raise ViewCloudedError("Board not recognized")
        else:
            return board_coordinates
    
    def get_board_cases(self, board_corner_coordinates):
        board_cases_coordinates = get_board_cases(board_corner_coordinates, self.config)
        return board_cases_coordinates

    def get_coordinates_of_square(self, square):
        case = case_to_realworld_coordinates(square)
        return case
    
    def get_stable_board_image(self):
        get_stable_image(self.reachy, self.config)