from .Enums.Board import Board
from .Enums.Outside import Outside
from .Enums.Animation import Animation
from .Enums.Sentence import Sentence
from .MoveImpl import MoveImpl
from .OutsideBlockFacade import OutsideBlockFacade
from .Sentences.Speak import sentence_line

class MoveFacade:
    def __init__(self):
        self.block_manager = OutsideBlockFacade()
        self.move = MoveImpl()
        
        """ 
        False: Use predefined unused block positions
        True: Utilize perceptions "get_nearest_unused_piece()" 
        """
        self.mode_detected_blocks = False
        self.mode_playing_sounds = False

    def set_dependencies(self, reachy, perc, strat):
        self.move.set_dependencies(reachy, perc, strat)

    def set_mode_to_detecting_blocks(self):
        # True: Utilize perceptions "get_nearest_unused_piece()" 
        self.mode_detected_blocks = True
    
    def set_mode_to_playing_sounds(self):
        self.mode_playing_sounds = True

    # TESTING REQUIRED: outside blocks are detected by perception.
    def do_move_block_v2_auto_detect_outside_block(self, to_board_pos: Board):
        self.move.start_move_object_as_threads(to_board_pos)

    def do_move_block(self, from_enum: Outside, to_enum: Board):
        """
        Calls a Function to move a Block to Board.
        Mode 1: Utilizing Predefined Positions for the Outside Blocks
        Mode 2: Utilizing Outside Block Detection via Perception 
        #TODO: Variable to change Modes easily
        """
        if not self.mode_detected_blocks:
            self.move.move_object(position_from=from_enum.value, position_to=to_enum) # Mode 1
        else:
            pos_from = self.move.detecting_nearest_block()
            self.move.move_object(pos_from, to_enum) # Mode 2

    def do_move_head(self, look_at: list):
        self.move.reachy.turn_on('head')
        self.move.move_head(look_at)
        self.move.reachy.turn_off_smoothly('head')

    def do_activate_right_arm(self):
        self.move.activate_right_arm()

    def do_pos_above_block_5(self):
        self.move.gotoposabove5()
    
    def do_deactivate_reachys_joints(self):
        self.move.reachy.turn_off_smoothly("reachy")

    def do_deactivate_right_arm(self):
        self.move.deactivate_right_arm()

    def do_deactivate_left_arm(self):
        self.move.deactivate_left_arm()

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

    def do_say(self, sentence_type: Sentence):
        if(self.mode_playing_sounds):
            sentence_line(sentence_type)

    def steal_block(self, f: Board):
        self.move.steal_object(f)