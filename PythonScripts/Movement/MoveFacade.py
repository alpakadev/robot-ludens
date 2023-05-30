from .MoveImpl import MoveImpl
from .InterruptImpl import InterruptImpl
from .OutsideBlockFacade import OutsideBlockFacade
from .Enums.Board import Board
from .Enums.Outside import Outside


class MoveFacade:
    def __init__(self):
        self.block_manager = OutsideBlockFacade()
        self.move = MoveImpl()
        self.interrupt = InterruptImpl()

    def set_dependencies(self, reachy, perc, strat):
        self.move.set_dependencies(reachy, perc, strat)

    def do_move_block(self, from_enum :Outside, to_enum: Board):
        return self.move.move_object(pos_from_enum=from_enum, pos_to_enum=to_enum)
        # return self.move.move_object(pos_from=self.block_manager.take_block(), pos_to=to)
    
    def do_move_head(self, look_at : list):
        # look_at: [x, y, z]
        self.move.move_head(look_at)

    def do_deactivate_right_arm(self):
        self.move.deactivate_right_arm()
    
    def do_calibration(self):
        self.move.calibrate()
