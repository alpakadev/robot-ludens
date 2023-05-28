from .MoveImpl import MoveImpl
from .InterruptImpl import InterruptImpl
from .OutsideBlockFacade import OutsideBlockFacade
from .Enums.Board import Board


class MoveFacade:
    def __init__(self):
        self.block_manager = OutsideBlockFacade()
        self.move = MoveImpl()
        self.interrupt = InterruptImpl()

    def set_dependencies(self, reachy, perc, strat):
        self.move.set_dependencies(reachy, perc, strat)

    def do_move_block(self, to: Board):
        return self.move.move_object(pos_from=self.block_manager.take_block(), pos_to=to)
    
    def do_move_head(self, look_at : list):
        # look_at: [x, y, z]
        self.move.move_head(look_at)

    def do_interrupt_move(self):
        return self.interrupt.do_interrupt_move()
