from Helpers.movement import goal_position
from Helpers.movement import base_position
from Helpers.image_stability import get_stable_image

class Helpers:
    def __init__(self, reachy, config):
        self.reachy = reachy
        self.config = config
    
    def get_stable_image(self):
        return get_stable_image(self.reachy, self.config)

    def move_head_to_goal_position(self):
        goal_position(self.reachy)

    def move_head_to_base_position(self):
        base_position(self.reachy)