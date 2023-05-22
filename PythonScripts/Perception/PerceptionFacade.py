from PerceptionImpl import PerceptionImplementation

class PerceptionFacade:
    def __init__(self, reachy):
        self.perception_implentation = PerceptionImplementation(reachy)
        self.move = None
        self.strat = None
    
    def get_game_state(self):
        return self.perception_implentation.get_game_state()
    
    def check_game_state_validity(self, state):
        return self.perception_implentation.check_state_validity(state)
    
    def get_coordinates_of_square(self, square):
        return self.perception_implentation.get_coordinates_of_square(square)
    
    def get_nearest_unused_piece(self):
        """Returns fixed position of the nearest available token not currently in the game"""
        return self.perception_implentation.get_nearest_unused_piece()

    def set_dependencies(self, move, strat):
        self.move = move
        self.strat = strat