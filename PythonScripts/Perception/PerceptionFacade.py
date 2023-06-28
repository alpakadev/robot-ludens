from .PerceptionImpl import PerceptionImplementation

class PerceptionFacade:
    def __init__(self, reachy):
        self.perception_implementation = PerceptionImplementation(reachy)
        self.move = None
        self.strat = None
    
    def get_game_state(self):
        # Gibt den Spielstand als 2D Array zurück
        return self.perception_implementation.get_game_state(self.move)
    
    def check_game_state_validity(self, state):
        # Gibt zurück, ob der angebene state valide ist. Bei nicht Übereinstimmung werden Zeile und Spalte des Fehlers zurückgegeben
        # Rückgabewert: boolean, dict
        return self.perception_implementation.check_state_validity(state)
    
    def get_coordinates_of_square(self, square):
        # Gibt die Echt-Welt Koordinaten eines gegbeen Squares zurück
        return self.perception_implementation.get_coordinates_of_square(square)
    
    def get_nearest_unused_piece(self):
        #Returns fixed position of the nearest available token not currently in the game
        return self.perception_implementation.get_nearest_unused_piece()

    def get_already_placed_pieces_coordinates(self):
        #Returns the midpoint coordinates of every token within the gameboard
        return self.perception_implementation.get_already_placed_pieces_coordinates()

    def set_dependencies(self, move, strat):
        # Übergibt die Singletons des Movement und Strategie Moduls an unsere Klasse
        self.move = move
        self.strat = strat
