import yaml
from .BoardPerception.BoardPerception import BoardPerception
from .GameState.GameState import GameState
from .Helpers.Helpers import Helpers
from .Exceptions.Exceptions import ViewCloudedError
from .PiecePerception.PiecePerception import PiecePerception
import cv2
from Movement.MoveFacade import MoveFacade 
from .FaceRecognition.FaceRecognition import FaceRecognition

class PerceptionImplementation:
    def __init__(self, reachy, move):
        self.config = yaml.safe_load(open("PythonScripts/Perception/config.yml"))
        self.board_perception = BoardPerception(self.config)
        self.game_state = GameState()
        self.piece_perception = PiecePerception(self.config)
        self.helpers = Helpers(reachy, self.config)
        self.face_recognition = FaceRecognition()
        self.reachy = reachy
        self.move = move

    def get_non_moving_image(self, move:MoveFacade):
        self.helpers.move_head_to_goal_position(move)
        frame = self.helpers.get_stable_image()
        return frame
            
    def get_game_state(self, move:MoveFacade):
        # Returns current state of the board
        frame = self.get_non_moving_image(move)
        try:
            board_corners = self.board_perception.get_board_corners(frame)
            board_cases_coordinates = self.board_perception.get_board_cases(board_corners)
            game_state = self.game_state.get_game_state(frame, board_cases_coordinates, self.config)
            self.helpers.move_head_to_base_position(move)
            return game_state
        except ViewCloudedError:
            self.helpers.move_head_to_base_position(move)
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

    def get_nearest_unused_piece(self, move):
        # Gibt Position des nähesten freien Spielsteins 
        # in der Form (X, Y) zurück
        # @return: (float, float)
        frame = self.get_non_moving_image(move)
        board_corners = self.board_perception.get_board_corners(frame)
        nearest_piece = self.piece_perception.get_nearest_unused_piece(frame, 
                                                                       board_corners)
        return nearest_piece

    def get_already_placed_pieces_coordinates(self):
        # Gibt Mittelpunkte aller grünen sowie roten Spielsteine, die bereits auf dem Feld stehen, mittels eines Arrays zurück
        # Beispielhafter Rückgabewert:
        # [0, 0, 0, 0, 0, (-5.9299755, 17.198578, 'G'), 0, 0, 0]
        frame = self.get_non_moving_image()
        board_corners = self.board_perception.get_board_corners(frame)
        board_cases_coordinates = self.board_perception.get_board_cases(board_corners)
        red_midpoints, green_midpoints = self.piece_perception.get_all_pieces_coordinates(
            frame, 
            board_corners, 
            board_cases_coordinates)
        return red_midpoints, green_midpoints


    def check_for_unused_pieces(self, frame):
        # Untersucht den aktuellen Frame nach ungenutzen Spielsteinen
        # Implementation in /PiecePerception/unused_pieces_detection.py
        unused_pieces = self.piece_perception.get_unused_pieces_from_frame(frame)
        return unused_pieces

    def identify_human_player(self):
        self.face_recognition.identify_human_player(self.reachy, self.move)
    
    def look_at_human_player(self):
        self.face_recognition.look_at_human_player(self.reachy, self.move)