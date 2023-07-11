import yaml
from .BoardPerception.BoardPerception import BoardPerception
from .GameState.GameState import GameState
from .PiecePerception.PiecePerception import PiecePerception
import cv2
from Movement.MoveFacade import MoveFacade 
from .FaceRecognition.FaceRecognition import FaceRecognition

class PerceptionImplementation:
    def __init__(self, reachy, move):
        self.config = yaml.safe_load(
            open("PythonScripts/Perception/config.yml")
        )
        self.board_perception = BoardPerception(reachy, self.config)
        self.game_state = GameState()
        self.piece_perception = PiecePerception(self.config)
        self.face_recognition = FaceRecognition()
        self.reachy = reachy
        self.move = move

    def _get_non_moving_image(self, move:MoveFacade):
        # Returns image with still non blurred view of board
        try:
            move.do_move_head([0.5, 0, -0.6])
        except NotImplementedError:
            # Check if current Setting is Simulation
            reachy.head.look_at(0.5, 0, -0.6, 1, "simul")
        frame = self.board_perception.do_get_stable_board_image()
        return frame
            
    def get_game_state(self, move:MoveFacade):
        # Returns current state of the board
        frame = self._get_non_moving_image(move)
        try:
            board_corners = self.board_perception.do_get_board_corners(frame)
            board_cases_coordinates = self.board_perception \
                                          .do_get_board_cases(board_corners)
            game_state = self.game_state.do_get_game_state(
                frame, 
                board_cases_coordinates, 
                self.config
            )
            try:
                move.do_move_head([0.5, 0, -0.6])
            except NotImplementedError:
                reachy.head.look_at(0.5, 0, -0.6, 1, "simul")

            return game_state
        except IndexError:
            try:
                move.do_move_head([0.5, 0, -0.6])
            except NotImplementedError:
                reachy.head.look_at(0.5, 0, -0.6, 1, "simul")
            print("Faulty Image, please try again")

    def get_nearest_unused_piece(self, move):
        # Returns position of nearest unused piece
        # Output format = (X, Y)
        # @return: (float, float)
        frame = self._get_non_moving_image(move)
        try:
            board_corners = self.board_perception \
                                .do_get_board_corners(frame)
            nearest_piece = self.piece_perception \
                                .do_get_nearest_unused_piece(frame, board_corners)
            return nearest_piece
        except IndexError:
            print("No nearest Unused Piece found!")

    def get_already_placed_pieces_coordinates(self, move):
        # Returns center of all pieces already on the board
        # Output: Array with length 9
        # Array Element: (X, Y, color)
        # Example: [0, 0, 0, 0, 0, (-5.9299755, 17.198578, 'G'), 0, 0, 0]
        frame = self._get_non_moving_image(move)
        try:
            board_corners = self.board_perception.do_get_board_corners(frame)
            board_cases_coordinates = self.board_perception \
                                          .do_get_board_cases(board_corners)
            red_midpnts, green_midpnts = self.piece_perception \
                                             .do_get_all_pieces_coordinates(
                                                frame, 
                                                board_corners, 
                                                board_cases_coordinates
                                             )
            return red_midpnts, green_midpnts
        except IndexError:
            print("No sufficient board state provided!")


    def check_for_unused_pieces(self, frame):
        # Checks current frame for unused pieces
        # Implementation in /PiecePerception/unused_pieces_detection.py
        unused_pieces = self.piece_perception \
                            .get_unused_pieces_from_frame(frame)
        return unused_pieces

    def identify_human_player(self):
        self.face_recognition.do_identify_human_player(self.reachy, self.move)
    
    def look_at_human_player(self):
        self.face_recognition.do_look_at_human_player(self.reachy, self.move)