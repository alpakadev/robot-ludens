from MoveImpl import MoveImpl
from InterruptImpl import InterruptImpl


class MoveFacade:
    def __init__(self):
        self.move = MoveImpl()
        self.interrupt = InterruptImpl()

    def do_move_block(self, frm, to):
        return self.move.do_move_block(frm, to)

    def do_interrupt_move(self):
        return self.interrupt.do_interrupt_move()
