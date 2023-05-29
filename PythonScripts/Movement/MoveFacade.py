from .MoveImpl import MoveImpl
from .InterruptImpl import InterruptImpl
from .OutsideBlockFacade import OutsideBlockFacade
from .Enums.Board import Board
from .Enums.Outside import Outside
from Enums.Animation import Animation


class MoveFacade:
    def __init__(self):
        self.block_manager = OutsideBlockFacade()
        self.move = MoveImpl()
        self.interrupt = InterruptImpl()

    def set_dependencies(self, reachy, perc, strat):
        self.move.set_dependencies(reachy, perc, strat)

    def do_move_block(self, from_enum: Outside, to_enum: Board):
        return self.move.move_object(pos_from_enum=from_enum, pos_to_enum=to_enum)

    def do_move_head(self, look_at: list):
        # look_at: [x, y, z]
        self.move.move_head(look_at)

    def do_animation(self, animation_type: Animation):
        self.move.perform_animation(animation_type)

    def do_interrupt_move(self):
        return self.interrupt.do_interrupt_move()
