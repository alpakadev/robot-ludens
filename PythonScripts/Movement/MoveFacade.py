from .Enums.Board import Board
from .Enums.Outside import Outside
from .Enums.Animation import Animation
from .MoveImpl import MoveImpl
from .OutsideBlockFacade import OutsideBlockFacade
from PythonScripts.Perception.PerceptionFacade import PerceptionFacade


class MoveFacade:
    def __init__(self, reachy):
        self.reachy = reachy
        self.block_manager = OutsideBlockFacade()
        self.perception = PerceptionFacade(reachy)
        self.move = MoveImpl()

    def set_dependencies(self, perc, strat):
        self.move.set_dependencies(self.reachy, perc, strat)

    # TESTING REQUIRED: outside blocks are detected by perception.
    def do_move_block_v2_auto_detect_outside_block(self, to_board_pos: Board):
        nearest_outside_block = self.perception.get_nearest_unused_piece()
        return self.move.start_move_object_requires_b_wahrnehmung_2(nearest_outside_block, to_board_pos)

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

    def do_safe_arm_pos(self):
        self.do_activate_right_arm()
        self.do_right_angled_position()
        self.do_pos_above_block_5()

    def do_animation(self, animation_type: Animation):
        self.move.perform_animation(animation_type)
