import time

from reachy_sdk import ReachySDK
from reachy_sdk.trajectory import goto
from reachy_sdk.trajectory.interpolation import InterpolationMode

from . import constants
from .Animations.Win import animation_win
from .Animations.Loose import animation_loose
from .Animations.Angry import animation_angry
from .Animations.Thinking import animation_thinking
from .Animations.Disapproval import animation_disapproval
from .Enums.Animation import Animation
from .Enums.Board import Board
from .Enums.Outside import Outside
from .Helper.KinematicModelHelper import KinematicModelHelper
from .Helper.HandRotationMapper import HandRotationMapper


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
        # The origin point, to which all other coordinates of the Board and the Blocks are relative.
        self.origin = constants.ORIGIN_COORDINATES

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

    def get_origin(self):
        # Returns the origin point to which all other coordinates are relative from
        return self.origin_coordinate

    def set_origin(self, coordinate):
        # Returns the origin point to which all other coordinates are relative from
        self.origin_coordinate = coordinate

    def activate_right_arm(self):
        self.reachy.turn_on("r_arm")

    def deactivate_right_arm(self):
        self.reachy.turn_off_smoothly("r_arm")

    def move_object(self, position_from: Outside, position_to: Board):
        self.activate_right_arm()
        self.move_head(constants.HEAD_LOOK_DOWN)
        mapper = HandRotationMapper()
        
        self._grip_open()
        self._grip_close()

        position_from_coordinates = position_from.value
        position_to_coordinates = position_to.value
        #Coordinate of Block 5 is added to origin Point
        temp_waiting_point = add_lists(self.origin, Outside.BLOCK_5.value) #####WIEDER ZU 5 ÄNDERN!!!!
        #First waiting point ist 15 cm above Block 5
        point_above_Block_5 = add_lists(temp_waiting_point, [0,0,0.15])
        #Second waiting point is 20 cm closer to Reachy (Above Block 1)
        point_above_Block_1 = add_lists(point_above_Block_5, [-0.17,0,0])

        
        position_to_coordinates = add_lists(self.origin, position_to_coordinates)
        position_from_coordinates = add_lists(self.origin, position_from_coordinates)
        #move to save point above origin point
        print(point_above_Block_5)
        print(point_above_Block_1)
        #Go to Right angle, WP1 and then WP2
        #self.set_arm_to_right_angle_position()
        self._move_arm(point_above_Block_5, rotation={'y': -90, 'x': 0, 'z': 0})
        self._move_arm(point_above_Block_1, rotation={'y': -90, 'x': 0, 'z': 0})



        position_from_coordinates[1] += constants.DELTA_HAND_WIDTH
        #Higher to not touch the table
        position_from_coordinates[2] += 0.1
        position_from_coordinates[0] -= constants.DELTA_FRONT
        self._move_arm(position_from_coordinates, rotation={'y': -90, 'x': 0, 'z': 0})
        #Move Delta before cylinder to be taken
        position_from_coordinates[2] -= 0.08
        self._move_arm(position_from_coordinates, rotation={'y': -90, 'x': 0, 'z': 0})
        #Calculate next move
        position_from_coordinates[0] += constants.DELTA_FRONT

        self._grip_open()
        #Moves Hand/arm to the cylinder
        self._move_arm(position_from_coordinates, rotation={'y': -90, 'x': 0, 'z': 0})
        #closes Hand
        self._grip_close()
        #Take cylinder up
        position_from_coordinates[2] += constants.DELTA_HEIGHT
        self._move_arm(position_from_coordinates, rotation={'y': -90, 'x': 0, 'z': 0})
        #Calculate and move to position about the goal
        position_to_coordinates[2] += constants.DELTA_HEIGHT
        self._move_arm(position_to_coordinates, rotation={'y': -90, 'x': 0, 'z': mapper.get_hand_rotation(
            position_to)})
        position_to_coordinates[2] -= constants.DELTA_HEIGHT
        #This is the lowest possible position for Reachy not to touch the other blocks
        #position_to_coordinates[2] += constants.DELTA_SAFE_HEIGHT

        # 7. moves arm to pos_to/Put Gripper down to get lower
        self._move_arm(position_to_coordinates,
                       rotation={'y': -70, 'x': 0, 'z': mapper.get_hand_rotation(position_to)})
        self._grip_open()
        position_to_coordinates[2] += constants.DELTA_HEIGHT
        self._move_arm(position_to_coordinates,
                       rotation={'y': -90, 'x': 0, 'z': mapper.get_hand_rotation(position_to)})
        position_to_coordinates[2] -= constants.DELTA_HEIGHT
        self._grip_close()
        # 10. Moves arm back to a save position
        #self._grip_close()
        self._move_arm(point_above_Block_5, rotation={'y': -90, 'x': 0, 'z': 0})


    def move_object_v2(self, position_from: Outside, position_to: Board):
        """
        Moves Object from A (pos_from) to B (pos_to)

        :param position_from: Coordinates where the Object to move is
        :param position_to: Coordinates on where to move the object
        """
        self.activate_right_arm()
        self.set_arm_to_right_angle_position()

        position_to_coordinates = add_lists(self.origin, position_to_coordinates)
        position_from_coordinates = add_lists(self.origin, position_from_coordinates)
        

        mapper = HandRotationMapper()

        position_from_coordinates = position_from.value
        position_to_coordinates = position_to.value

        # Adds the position values to base position - Since the Enums are dependent of the Base Position
        position_to_coordinates = add_lists(self.origin, position_to_coordinates)
        position_from_coordinates = add_lists(self.origin, position_from_coordinates)

        # Tiefe == x (nach vorne), breite == z , Hoehe ==y
        position_from_coordinates[1] += constants.DELTA_HAND_WIDTH  # Non Moving Part of Hand would knock Items over
        # starting movement of reachy's head
        self.move_head(constants.HEAD_LOOK_DOWN)
        time.sleep(1.0)
        self.move_head(constants.HEAD_LOOK_FRONT)
        self.move_head()
        # 1. Moves arm in front of the Object
        position_from_coordinates[0] -= constants.DELTA_FRONT
        self._move_arm(position_from_coordinates, rotation={'y': -90, 'x': 0, 'z': 0})
        position_from_coordinates[0] += constants.DELTA_FRONT
        self.move_head()
        # 2. Opens Hand
        self._grip_open()
        # 3. Moves Hand/arm to the object
        self._move_arm(position_from_coordinates, rotation={'y': -90, 'x': 0, 'z': 0})
        # 4. closes Hand
        self._grip_close()
        # 5. Moves arm above current position
        position_from_coordinates[2] += constants.DELTA_HEIGHT
        self._move_arm(position_from_coordinates, rotation={'y': -90, 'x': 0, 'z': 0})
        position_from_coordinates[2] -= constants.DELTA_HEIGHT
        # self.move_head(pos_goal)
        # 6. Moves arm above pos_to
        position_to_coordinates[2] += constants.DELTA_HEIGHT
        self._move_arm(position_to_coordinates, rotation={'y': -90, 'x': 0, 'z': mapper.get_hand_rotation(
            position_to)})  ##TODO: How to Handle POS_ABOVE_BOARD?
        position_to_coordinates[2] -= constants.DELTA_HEIGHT
        self.move_head()
        # 7. moves arm to pos_to
        self._move_arm(position_to_coordinates,
                       rotation={'y': -90, 'x': 0, 'z': mapper.get_hand_rotation(position_to)})
        # 8. opens Hand
        self._grip_open()
        # 9. Moves arm up
        position_to_coordinates[2] += constants.DELTA_HEIGHT
        self._move_arm(position_to_coordinates,
                       rotation={'y': -90, 'x': 0, 'z': mapper.get_hand_rotation(position_to)})
        position_to_coordinates[2] -= constants.DELTA_HEIGHT
        self.move_head()
        # 10. Moves arm back to a save position
        self._grip_close()
        self.set_arm_to_right_angle_position()
        # 11. Moving arm to the origin coordinate, so that it does not block the view
        self._move_arm(add_lists(self.origin, [0, -0.085, 0.10]), rotation={'y': -90, 'x': 0, 'z': 0})

        # Setting arm to compliant mode and lowering smoothly for preventing damaging
        # self.deactivate_right_arm()
        # head back to default and setting head to compliant mode
        self.move_head(constants.HEAD_LOOK_FRONT)

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
        print(self.get_origin())

    def move_head(self, look_at=None):
        """
        Moves reachy's head either by the given coordinates defined by look_at or
        follows the right arm's coordinates

        """
        self.reachy.turn_on("head")

        # Head follows arm
        if look_at is None:
            x, y, z = self.reachy.r_arm.forward_kinematics()[:3, -1]
            self.reachy.head.look_at(x=x, y=y, z=z - 0.05, duration=1.0)

        # Head looks at given x,y,z
        else:
            x, y, z = look_at
            self.reachy.head.look_at(x=x, y=y, z=z, duration=1.0)

        self.reachy.turn_off_smoothly("head")

    def perform_animation(self, animation_type: Animation):
        match animation_type:
            case Animation.WIN:
                animation_win(self.reachy)
            case Animation.LOOSE:
                animation_loose(self.reachy)
            case Animation.ANGRY:
                animation_angry(self.reachy)
            case Animation.THINKING:
                animation_thinking(self.reachy)
            case Animation.DISAPPROVAL:
                animation_disapproval(self.reachy)
