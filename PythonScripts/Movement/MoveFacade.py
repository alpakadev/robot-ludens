from .Enums.Board import Board
from .Enums.Outside import Outside
from .Enums.Animation import Animation
from .MoveImpl import MoveImpl
from .OutsideBlockFacade import OutsideBlockFacade


class MoveFacade:
    def __init__(self):
        self.block_manager = OutsideBlockFacade()
        self.move = MoveImpl()

    def set_dependencies(self, reachy, perc, strat):
        self.move.set_dependencies(reachy, perc, strat)

    def do_move_block(self, from_enum: Outside, to_enum: Board):
        return self.move.move_object(position_from=from_enum, position_to=to_enum)

    def do_move_head(self, look_at: list):
        self.move.move_head(look_at)

    def do_activate_right_arm(self):
        self.move.activate_right_arm()

    def do_pos_above_block_5(self):
        self.move.gotoposabove5()

    def do_deactivate_right_arm(self):
        self.move.deactivate_right_arm()

    def do_calibration(self):
        self.move.calibrate()

    def do_right_angled_position(self):
        self.move.set_arm_to_right_angle_position()

    def do_grip_open(self):
        self.move._grip_open()

    def do_grip_close(self):
        self.move._grip_close()

    def do_animation(self, animation_type: Animation):
        self.move.perform_animation(animation_type)
