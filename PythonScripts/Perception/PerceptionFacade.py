from .PerceptionImpl import PerceptionImplementation

class PerceptionFacade:
    def __init__(self):
        self.move = None
        self.strat = None
        self.reachy = None
        self.perception_implementation = PerceptionImplementation(None, None)
    
    
    def get_game_state(self):
        # Gibt den Spielstand als 2D Array zurück
        return self.perception_implementation.get_game_state(self.move)
    
    def get_nearest_unused_piece(self):
        # Returns fixed position of the nearest available token 
        # If token not currently in the game
        return self.perception_implementation.get_nearest_unused_piece(
            self.move
        )
    
    def identify_human_player(self):
        self.perception_implementation.identify_human_player()
    
    def look_at_human_player(self):
        self.perception_implementation.look_at_human_player()

    def get_already_placed_pieces_coordinates(self):
        #Returns the midpoint coordinates of every token within the gameboard
        return self.perception_implementation \
                   .get_already_placed_pieces_coordinates()

    def set_dependencies(self, reachy, move, strat):
        self.reachy = reachy
        self.move = move
        self.strat = strat
        self.perception_implementation = PerceptionImplementation(reachy, move)