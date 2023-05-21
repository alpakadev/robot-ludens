from PerceptionImpl import PerceptionImplementation

class PerceptionFacade:
    def __init__(self):
        self.perception_implentation = None
        self.move = None
        self.strat = None
    
    def get_game_state(self):
        return self.perception_implentation.get_game_state()
    
    def check_game_state_validity(self, state):
        return self.perception_implentation.check_state_validity(state)
    
    def get_coordinates_of_square(self, square):
        return self.perception_implentation.get_coordinates_of_square(square)

    def set_dependencies(self, reachy, move, strat):
        self.perception_implentation = PerceptionImplementation(reachy)
        self.move = move
        self.strat = strat