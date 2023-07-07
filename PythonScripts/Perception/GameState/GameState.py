from .game_state_detection import get_board_state

class GameState:
    pass


    def get_game_state(self, frame, cases_coords, config):
        return get_board_state(frame, cases_coords, config)