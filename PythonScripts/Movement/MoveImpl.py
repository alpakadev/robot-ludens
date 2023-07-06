import time

from reachy_sdk import ReachySDK
from reachy_sdk.trajectory import goto
from reachy_sdk.trajectory.interpolation import InterpolationMode
from threading import Thread

from . import constants
from .Animations.Win import animation_win
from .Animations.Lose import animation_lose
from .Animations.Angry import animation_angry
from .Animations.Thinking import animation_thinking
from .Animations.Disapproval import animation_disapproval
from .Animations.SadAntennas import animation_sad_antennas
from .Animations.HappyAntennas import animation_happy_antennas
from .Animations.Inhale import animation_inhale
from .Animations.Level0 import animation_level0
from .Animations.Level1 import animation_level1
from .Animations.Level2 import animation_level2
from .Animations.Level3 import animation_level3
from .Animations.Level4 import animation_level4
from .Animations.Tie import animation_tie
from .Animations.StartReachy import animation_start_reachy
from .Animations.StartOpponent import animation_start_opponent
from .Animations.Forward import animation_forward
from .Animations.Clueless import animation_clueless
from .Animations.Happy import animation_happy

from .Enums.Animation import Animation
from .Enums.Board import Board
from .Enums.Outside import Outside
from .Helper.KinematicModelHelper import KinematicModelHelper
from .Helper.HandRotationMapper import HandRotationMapper

import threading
import sys




def add_lists(a, b):
    c = a[::]
    for i in range(len(c)):
        c[i] += b[i]
    return c


class MoveImpl:


    def __init__(self):
        self.strategy = None
        self.perception = None
        self.reachy = None
        self.POS_GRIPPER = None
        self.kinematic_model_helper = KinematicModelHelper()
        self.mapper = HandRotationMapper()
        # The origin point, to which all other coordinates of the Board and the Blocks are relative.
        self.origin = constants.ORIGIN_COORDINATES
        self.move_finished = True

    def set_dependencies(self, reachy: ReachySDK, perc, strat):
        self.reachy = reachy
        self.perception = perc
        self.strategy = strat
        # Defines Dictionary for modifying the gripping force - Needs reachy defined first
        self.POS_GRIPPER = {self.reachy.r_arm.r_gripper: 0}

    def get_origin(self):
        """
        Returns the origin point to which all other coordinates are relative from
        """
        return self.origin

    def set_origin(self, coordinate):
        self.origin = coordinate

    def set_arm_to_right_angle_position(self):
        self._move_arm(constants.POS_ARM_AT_RIGHT_ANGLE, rotation={'y': -90, 'x': 0, 'z': 0})

    def set_arm_to_origin(self):
        self._move_arm(self.origin, rotation={'y': -90, 'x': 0, 'z': 0})

    def activate_right_arm(self):
        self.reachy.turn_on("r_arm")

    def deactivate_right_arm(self):
        self.reachy.turn_off_smoothly("r_arm")

    def gotoposabove5(self):
        self.activate_right_arm()
        temp_waiting_point = add_lists(self.origin, Outside.BLOCK_5.value)
        point_above_Block_5 = add_lists(temp_waiting_point, [0, 0, 0.2])
        self._move_arm(point_above_Block_5, rotation={'y': -90, 'x': 0, 'z': 0})
    
    def set_arm_to_side_position(self):
        self._move_arm(constants.POS_ARM_SIDE, rotation={'y': -90, 'x': 0, 'z': 90})

    def move_object(self, position_from: Outside, position_to: Board):
        self.move_finished = False
        self.reachy.turn_on("head")
        self.activate_right_arm()
        self.move_head(constants.HEAD_LOOK_DOWN)

        position_from_coordinates = position_from.value
        position_to_coordinates = position_to.value

        position_to_coordinates = add_lists(self.origin, position_to_coordinates)
        position_from_coordinates = add_lists(self.origin, position_from_coordinates)

        thread1 = threading.Thread(target=self.head_follows_arm)
        thread1.start()

        #calculate coordinate above block 5
        temp_waiting_point = add_lists(self.origin, Outside.BLOCK_5.value)
        point_above_Block_5 = add_lists(temp_waiting_point, [0,0,0.2])
        point_above_Block_1 = add_lists(point_above_Block_5, [-0.17,0,0])

        self._move_arm(point_above_Block_5, rotation={'y': -90, 'x': 0, 'z': 0})
        self._move_arm(point_above_Block_1, rotation={'y': -90, 'x': 0, 'z': 0})

        # Add hand width
        position_from_coordinates[1] += constants.DELTA_HAND_WIDTH

        position_from_coordinates[2] += 0.15
        position_from_coordinates[0] -= constants.DELTA_FRONT
        self._move_arm(position_from_coordinates, rotation={'y': -90, 'x': 0, 'z': 0})

        position_from_coordinates[2] -= 0.11
        
        self._move_arm(position_from_coordinates, rotation={'y': -90, 'x': 0, 'z': 0})

        
        self._grip_open()

        position_from_coordinates[0] += constants.DELTA_FRONT
        position_from_coordinates[0] += 0.02
        self._move_arm(position_from_coordinates, rotation={'y': -90, 'x': 0, 'z': 0})

        self._grip_close()

        position_from_coordinates[2] += 0.1
        self._move_arm(position_from_coordinates, rotation={'y': -90, 'x': 0, 'z': 0})

        #beginning of pos_to
        position_to_coordinates[2] += constants.DELTA_HEIGHT
        self._move_arm(position_to_coordinates, rotation={'y': -90, 'x': 0, 'z': self.mapper.get_hand_rotation(
            position_to)})
        
        position_to_coordinates[2] -= constants.DELTA_HEIGHT
        # Here neigung -70
        self._move_arm(position_to_coordinates, rotation={'y': -70, 'x': 0, 'z': self.mapper.get_hand_rotation(
            position_to)})
        
        self._grip_open()

        position_to_coordinates[2] += constants.DELTA_HEIGHT
        self._move_arm(position_to_coordinates, rotation={'y': -90, 'x': 0, 'z': self.mapper.get_hand_rotation(
            position_to)})

        self._grip_close()

        self._move_arm(point_above_Block_5, rotation={'y': -90, 'x': 0, 'z': 0})
        
        self.move_finished = True
        self.move_head(constants.HEAD_LOOK_DOWN)
        self.reachy.turn_off_smoothly("head")


    def head_follows_arm(self):
        """
        Head following the Hand Continiously until the Movement of a block is finished
        v1 Has to be called as a thread **inside** `move_object()`. 
        The movement function needs to set the Variable `move_finished` to True
        """
        self.move_head()
        time.sleep(0.5)
        while True:
            self.move_head()
            #time.sleep(0.5)
            if (self.move_finished):
                sys.exit()

    def head_follows_arm_v2(self, thread_moving_object: Thread):
        """
        Head following the Hand Continiously until the Movement of a block is finished
        v2 Has to be called **beside** `move_object()` in a parallel thread. 
        Finishes when the thread_moving_object finishes
        """
        self.move_head()
        time.sleep(0.5)
        while thread_moving_object.is_alive():
            self.move_head()

    def start_move_object_as_threads(self, goal: Board):
        """
        This function is an approach for Moving the head parallel to the arm
        It currently also is the function utilizing the detection of unused Blocks.
        
        TODO: Decide, where the arm should be moved when detecting Blocks
        """
        self.set_arm_to_side_position() # Temporary Position to move Arm out of the view
        start = self.perception.get_nearest_unused_piece() # returns list [x,y] coord
        start += [-0.05] # Adds [z] coordinate; Value Adjusted to `Outside.py`
        # start = Outside.BLOCK_1.value # Test: Taking predefined Position of Block 1
        self.gotoposabove5()
        print("Detected nearest Block at Coordinate: ", start)
        thread_moving_object = Thread(target=self.move_object, args=(start, goal))
        thread_head_following_hand = Thread(target=self.head_follows_arm_v2, args=[thread_moving_object])

        thread_moving_object.start()
        thread_head_following_hand.start()

        while thread_moving_object.is_alive() or thread_head_following_hand.is_alive():
            pass
        print("Movement threads have ended")


    def _move_arm(self, pos_to: list, rotation: dict):
        """
        Moving arm to Position

        """
        target_kinematic = self.kinematic_model_helper.get_kinematic_move(pose=pos_to, rotation=rotation)
        joint_pos_A = self.reachy.r_arm.inverse_kinematics(target_kinematic)
        goto({joint: pos for joint, pos in zip(self.reachy.r_arm.joints.values(), joint_pos_A)}, duration=2.0)

    def _change_grip_force(self, force):
        self.POS_GRIPPER[self.reachy.r_arm.r_gripper] = force
        # print("current force:", self.POS_GRIPPER[self.reachy.r_arm.r_gripper])

    def _grip_open(self):
        """
        opens grip completely
        """
        self._change_grip_force(constants.GRIPPER_OPEN_FULL)
        goto(goal_positions=self.POS_GRIPPER, duration=1.0, interpolation_mode=InterpolationMode.MINIMUM_JERK)

    def _grip_close(self):
        """
        closes grip until is_holding is true
        """
        self._change_grip_force(constants.GRIPPER_CLOSED)
        goto(goal_positions=self.POS_GRIPPER, duration=1.0, interpolation_mode=InterpolationMode.MINIMUM_JERK)

    def _is_holding(self):
        """
        :returns: 'True' if reachy`s right arm is holding something
        """
        # ERROR: force sensors gives too high values (> 10000); but code is equal to official
        # reachy documentation
        if self.reachy.force_sensors.r_force_gripper.force > constants.GRIP_FORCE_HOLDING:
            # TODO: Warning when to much Force is applied
            return True
        return False

    def move_body(self, x, y):
        """
        Moves the Reachy/Robot Body to given Coordinates
        !Obstacles are ignored/Undefined

        """
        self.reachy.mobile_base.goto(x, y, theta=0)

    def turn_body(self, degree):
        """
        Rotates the mobile base by a given angle (counterclockwise)

        :param degree: The angle to rotate
        """
        self.reachy.mobile_base.goto(x=0.0, y=0.0, theta=degree)

    def calibrate(self):
        matrix = self.reachy.r_arm.forward_kinematics()
        x = round(matrix[0][3], 2)
        y = round(matrix[1][3], 2)
        z = -0.37
        res = [x, y, z]
        self.set_origin(res)
        print("Calibration of bottem right corner: ",self.get_origin())

    def move_head(self, look_at=None):
        """
        Moves reachy's head either by the given coordinates defined by look_at or
        follows the right arm's coordinates

        """
        #self.reachy.turn_on("head")

        # Head follows arm
        if look_at is None:
            x, y, z = self.reachy.r_arm.forward_kinematics()[:3, -1]
            self.reachy.head.look_at(x=x, y=y, z=z - 0.05, duration=0.1)
            


        # Head looks at given x,y,z
        else:
            x, y, z = look_at
            self.reachy.head.look_at(x=x, y=y, z=z, duration=1.0)

        #self.reachy.turn_off_smoothly("head")

    def perform_animation(self, animation_type: Animation):
        match animation_type:
            case Animation.WIN:
                animation_win(self.reachy)
            case Animation.LOSE:
                animation_lose(self.reachy)
            case Animation.ANGRY:
                animation_angry(self.reachy)
            case Animation.THINKING:
                animation_thinking(self.reachy)
            case Animation.DISAPPROVAL:
                animation_disapproval(self.reachy)
            case Animation.SAD_ANTENNAS:
                animation_sad_antennas(self.reachy)
            case Animation.HAPPY_ANTENNAS:
                animation_happy_antennas(self.reachy)
            case Animation.INHALE:
                animation_inhale()
            case Animation.LEVEL0:
                animation_level0(self.reachy)
            case Animation.LEVEL1:
                animation_level1(self.reachy)
            case Animation.LEVEL2:
                animation_level2(self.reachy)
            case Animation.LEVEL3:
                animation_level3(self.reachy)
            case Animation.LEVEL4:
                animation_level4(self.reachy)
            case Animation.TIE:
                animation_tie(self.reachy)
            case Animation.START_REACHY:
                animation_start_reachy(self.reachy)
            case Animation.START_OPPONENT:
                animation_start_opponent(self.reachy)
            case Animation.FORWARD:
                animation_forward(self.reachy)
            case Animation.CLUELESS:
                animation_clueless(self.reachy)
            case Animation.HAPPY:
                animation_happy(self.reachy)
