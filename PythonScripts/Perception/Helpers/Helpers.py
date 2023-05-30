from .movement import goal_position
from .movement import base_position
from .image_stability import get_stable_image
from Movement.MoveFacade import MoveFacade 

class Helpers:
    def __init__(self, reachy, config):
        self.reachy = reachy
        self.config = config
    
    def get_stable_image(self):
        return get_stable_image(self.reachy, self.config)

    def move_head_to_goal_position(self, move: MoveFacade):
        goal_position(self.reachy, move)

    def move_head_to_base_position(self, move: MoveFacade):
        base_position(self.reachy, move)