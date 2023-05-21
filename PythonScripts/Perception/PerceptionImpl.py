import yaml
from BoardPerception.BoardPerception import BoardPerception
from GameState.GameState import GameState
from Helpers.Helpers import Helpers
from Exceptions.Exceptions import ViewClouded
import cv2

class PerceptionImplementation:
    def __init__(self, reachy):
        self.config = yaml.safe_load(open("PythonScripts/Perception/config.yml"))
        self.board_perception = BoardPerception(self.config)
        self.game_state = GameState()
        self.helpers = Helpers(reachy, self.config)

    def get_non_moving_image(self):
        self.helpers.move_head_to_goal_position()
        frame = self.helpers.get_stable_image()
        return frame
            
    def get_game_state(self):
        # Returns current state of the board
        frame = self.get_non_moving_image()
        try:
            board_corners = self.board_perception.get_board_corners(frame)
            board_cases_coordinates = self.board_perception.get_board_cases(board_corners)
            game_state = self.game_state.get_game_state(frame, board_cases_coordinates, self.config)
            self.helpers.move_head_to_base_position()
            return game_state
        except ViewClouded:
            self.helpers.move_head_to_base_position()
            return "Faulty Image, please try again"

    def check_state_validity(self, state):
        # state = [[x1, x2, x3], [y1, y2, y3], [z1, z2, z3]]
        # Check if board is still in the desired state
        mismatches = []
        new_state = self.get_game_state()
        if len(state) != len(new_state):
            return "Wrong input format"
        for i in range(0, len(state)):
            for j in range (0, len(state[i])):
                if state[i][j] != new_state[i][j]:
                    mismatches.append({"line": i, "square": j})
        if len(mismatches) > 0:
            return False, mismatches
        else:
            return True

    def get_coordinates_of_square(self, square):
        # Square = "TOP_LEFT_CORNER", "TOP_RIGHT_CORNER", "TOP_MIDDLE", "BOTTOM_LEFT_CORNER", "BOTTOM_RIGHT_CORNER", "BOTTOM_MIDDLE", "LEFT_MIDDLE", "RIGHT_MIDDLE", "CENTER"
        # Get Real World Coordinates of certain square
        return self.board_perception.get_coordinates_of_square(square)