# import sys
# sys.path.append('..') #For importing from Neighbour Folder
# Uncomment above if its not working
from ..Enums.Board import Board


class HandRotationMapper:
    def __init__(self):
        self.rotations = {
            'TOP_LEFT': 45,
            'TOP_CENTER': 45,
            'TOP_RIGHT': 0,
            'CENTER_LEFT': 45,
            'CENTER': 45,
            'CENTER_RIGHT': 0,
            'BOTTOM_LEFT': 90,
            'BOTTOM_CENTER': 90,
            'BOTTOM_RIGHT': 45,
        }

    def _map(self, pos_to: str):
        return self.rotations[pos_to]

    def get_hand_rotation(self, pos_to: Board):
        return self._map(pos_to.name)
