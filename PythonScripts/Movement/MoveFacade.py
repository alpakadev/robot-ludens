from .Enums.Animation import Animation
from .Enums.Board import Board
from .Enums.Outside import Outside
from .Enums.Sentence import Sentence
from .MoveImpl import MoveImpl
from .OutsideBlockFacade import OutsideBlockFacade
from .Sentences.Speak import sentence_line


class MoveFacade:
    def __init__(self):
        self.block_manager = OutsideBlockFacade()
        self.move = MoveImpl()

        """ 
        False: Verwende vordefinierte unbenutzte Blockpositionen
        True: Verwende Wahrnehmungen "get_nearest_unused_piece()"
        """
        self.mode_detected_blocks = False
        self.mode_playing_sounds = False

    def set_dependencies(self, reachy, perc, strat):
        """
        Setzt die Abhängigkeiten für die MoveImpl-Klasse.
        """
        self.move.set_dependencies(reachy, perc, strat)

    def set_mode_to_detecting_blocks(self):
        """
        Setzt den Modus zur Erkennung von Blöcken.
        Modus 2: Verwendung der Außenerkennung über die Wahrnehmungsschnittstelle (get_nearest_unused_piece()).
        """
        self.mode_detected_blocks = True

    def set_mode_to_playing_sounds(self):
        """
        Setzt den Modus zum Abspielen von Sounds auf True.
        """
        self.mode_playing_sounds = True

    def do_move_block_v2_auto_detect_outside_block(self, to_board_pos: Board):
        """
        Führt einen Blockverschiebevorgang unter Verwendung von Threads aus.
        Die Außenblöcke werden automatisch mithilfe der Wahrnehmungsschnittstelle erkannt.
        T1: Thread zum Bewegen des Objekts
        T2: Thread zum Verfolgen der Handbewegung mit dem Kopf
        """
        self.move.start_move_object_as_threads(to_board_pos)

    def do_move_block(self, from_enum: Outside, to_enum: Board):
        """
        Calls a Function to move a Block to Board.
        Mode 1: Utilizing Predefined Positions for the Outside Blocks
        Mode 2: Utilizing Outside Block Detection via Perception 
        #TODO: Variable to change Modes easily
        """
        if not self.mode_detected_blocks:
            self.move.move_object(position_from=from_enum.value, position_to=to_enum)  # Mode 1
        else:
            pos_from = self.move.detecting_nearest_block()
            self.move.move_object(pos_from, to_enum)  # Mode 2

    def do_move_head(self, look_at: list):
        """
        Bewegt den Kopf zur gegebenen Blickrichtung.
        Der Kopf wird eingeschaltet, wenn die Methode aufgerufen wird, und am Ende ausgeschaltet.
        """
        self.move.reachy.turn_on('head')
        self.move.move_head(look_at)
        self.move.reachy.turn_off_smoothly('head')

    def do_activate_right_arm(self):
        self.move.activate_right_arm()

    def do_pos_above_block_5(self):
        """
        Bewegt den Arm in die Warteposition über Block fünf.
        """
        self.move.go_to_pos_above_5()

    def do_deactivate_reachys_joints(self):
        self.move.reachy.turn_off_smoothly("reachy")

    def do_deactivate_right_arm(self):
        self.move.deactivate_right_arm()

    def do_deactivate_left_arm(self):
        self.move.deactivate_left_arm()

    def do_calibration(self):
        """
        Kalibriert die Ursprungspositionen auf der unteren linken Ecke des Spielfelds
        mithilfe der Vorwärtskinematik des rechten Arms.
        """
        self.move.calibrate()

    def do_right_angled_position(self):
        self.move.set_arm_to_right_angle_position()

    def do_grip_open(self):
        self.move.grip_open()

    def do_grip_close(self):
        self.move.grip_close()

    def do_safe_arm_pos(self):
        """
        Führt eine Abfolge von Bewegungen aus, um den Arm in eine sichere Position zu bringen.
        """
        self.do_activate_right_arm()
        self.do_right_angled_position()
        self.do_pos_above_block_5()

    def do_animation(self, animation_type: Animation):
        self.move.perform_animation(animation_type, use_sound=self.mode_playing_sounds)

    def do_say(self, sentence_type: Sentence):
        if self.mode_playing_sounds:
            sentence_line(sentence_type)

    def steal_block(self, f: Board):
        """
        Entfernt einen Block.
        """
        self.move.steal_object(f)
