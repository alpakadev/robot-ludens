from Exceptions.Exceptions import ViewClouded
from BoardPerception.board_cases_detection import get_board_cases
from BoardPerception.case_to_realworld_coordinates import case_to_realworld_coordinates
from BoardPerception.game_board_detection import game_board_detection

class BoardPerception:
    def __init__(self, config):
        self.config = config
    
    def get_board_corners(self, frame):
        board_coordinates = game_board_detection(frame, self.config)
        if len(board_coordinates) < 4:
            raise ViewClouded("Board not recognized")
        else:
            return board_coordinates
    
    def get_board_cases(self, board_corner_coordinates):
        board_cases_coordinates = get_board_cases(board_corner_coordinates, self.config)
        return board_cases_coordinates

    def get_coordinates_of_square(self, square):
        case = case_to_realworld_coordinates(square)
        return case