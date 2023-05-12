from MoveImpl import MoveImpl
from InterruptImpl import InterruptImpl
from ..OutsideBlockFacade import OutsideBlockFacade
from Enums.Board import Board


class MoveFacade:
    def __init__(self, reachy):
        self.block_manager = OutsideBlockFacade()
        self.move = MoveImpl(reachy)
        self.interrupt = InterruptImpl()

    def do_move_block(self, to: Board):
        return self.move.move_object(pos_from=self.block_manager.take_block(), pos_to=to.value)

    def do_interrupt_move(self):
        return self.interrupt.do_interrupt_move()