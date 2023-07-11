import sys
import threading
import time
from math import pow, sqrt
from threading import Thread

from reachy_sdk import ReachySDK
from reachy_sdk.trajectory import goto
from reachy_sdk.trajectory.interpolation import InterpolationMode

from . import constants
from .Animations.Angry import animation_angry
from .Animations.Clueless import animation_clueless
from .Animations.Disapproval import animation_disapproval
from .Animations.Forward import animation_forward
from .Animations.Happy import animation_happy
from .Animations.HappyAntennas import animation_happy_antennas
from .Animations.Level0 import animation_level0
from .Animations.Level1 import animation_level1
from .Animations.Level2 import animation_level2
from .Animations.Level3 import animation_level3
from .Animations.Lose import animation_lose
from .Animations.SadAntennas import animation_sad_antennas
from .Animations.StartOpponent import animation_start_opponent
from .Animations.StartReachy import animation_start_reachy
from .Animations.Thinking import animation_thinking
from .Animations.Tie import animation_tie
from .Animations.Win import animation_win
from .Enums.Animation import Animation
from .Enums.Board import Board
from .Enums.Outside import Outside
from .Helper.HandRotationMapper import HandRotationMapper
from .Helper.KinematicModelHelper import KinematicModelHelper


def add_lists(a, b):
    c = a[::]
    for i in range(len(c)):
        c[i] += b[i]
    return c


def sub_lists(a, b):
    c = a[::]
    for i in range(len(c)):
        c[i] -= b[i]
    return c


class MoveImpl:
    def __init__(self):
        """
        Initialisiert eine neue Instanz der MoveImpl-Klasse.
        """
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
        """
        Setzt die Abhängigkeiten für die MoveImpl-Klasse.

        :param reachy: Eine Instanz der ReachySDK-Klasse.
        :param perc: Die Perception-Instanz.
        :param strat: Die Strategy-Instanz.
        """
        self.reachy = reachy
        self.perception = perc
        self.strategy = strat
        # Defines Dictionary for modifying the gripping force - Needs reachy defined first
        self.POS_GRIPPER = {self.reachy.r_arm.r_gripper: 0}

    def get_origin(self):
        """
        Gibt den Ursprungspunkt zurück, auf den alle anderen Koordinaten bezogen sind.

        :return: Die Koordinaten des Ursprungspunkts.
        """
        return self.origin

    def set_origin(self, coordinate):
        """
        Setzt den Ursprungspunkt auf die angegebene Koordinate.

        :param coordinate: Die Koordinaten des Ursprungspunkts.
        """
        self.origin = coordinate

    def set_arm_to_right_angle_position(self):
        self._move_arm(
            constants.POS_ARM_AT_RIGHT_ANGLE, rotation={"y": -90, "x": 0, "z": 0}
        )

    def set_arm_to_origin(self):
        """
        Setzt den Arm auf den kalibrierten Ursprungspunkt.
        """
        self._move_arm(self.origin, rotation={"y": -90, "x": 0, "z": 0})

    def activate_right_arm(self):
        self.reachy.turn_on("r_arm")

    def deactivate_right_arm(self):
        self.reachy.turn_off_smoothly("r_arm")

    def deactivate_left_arm(self):
        self.reachy.turn_off_smoothly("l_arm")

    def go_to_pos_above_5(self):
        """
        Bewegt den Arm in die Warteposition über Block 5.
        """
        self.activate_right_arm()
        temp_waiting_point = add_lists(self.origin, Outside.BLOCK_5.value)
        point_above_Block_5 = add_lists(temp_waiting_point, [0, 0, 0.2])
        self._move_arm(point_above_Block_5, rotation={"y": -90, "x": 0, "z": 0})

    def set_arm_to_side_position(self):
        self._move_arm(constants.POS_ARM_SIDE, rotation={"y": -90, "x": 0, "z": 90})

    def move_object(self, position_from: list, position_to: Board):
        """
        Bewegt ein Objekt von der Position 'position_from' zur Position 'position_to'.

        :param position_from: Die Ausgangsposition des Objekts.
        :param position_to: Die Zielposition des Objekts.

        Note: "position_from" is not an "Outside"-Type anymore, since this function can
        be called with coordinates from dedected Blocks "get_nearest_unused_pieces()"
        """
        self.move_finished = False
        self.reachy.turn_on("head")
        self.activate_right_arm()
        self.move_head(constants.HEAD_LOOK_DOWN)

        # Define coordinates
        position_from_coordinates = position_from
        position_to_coordinates = position_to.value

        # Add coordinates to origin point
        position_to_coordinates = add_lists(self.origin, position_to_coordinates)
        position_from_coordinates = add_lists(self.origin, position_from_coordinates)

        # Starting Thread for head control
        thread1 = threading.Thread(target=self.head_follows_arm)
        thread1.start()

        # calculate coordinate above block 5 and block 1 (17cm from block 5 in y direction towards Reachy)
        temp_waiting_point = add_lists(self.origin, Outside.BLOCK_5.value)
        point_above_Block_5 = add_lists(temp_waiting_point, [0, 0, 0.2])
        point_above_Block_1 = add_lists(point_above_Block_5, [-0.17, 0, 0])

        # move arm to position above block 5 then above block 1
        ## Commented assuming Arm already is above Block 5
        # self._move_arm(point_above_Block_5, rotation={'y': -90, 'x': 0, 'z': 0})
        self._move_arm(point_above_Block_1, rotation={"y": -90, "x": 0, "z": 0})

        # Add hand width
        # position_from_coordinates[1] += constants.DELTA_HAND_WIDTH

        # Add safe height
        position_from_coordinates[2] += 0.15

        # Subtract constant distance (pull hand back)
        position_from_coordinates[0] -= constants.DELTA_FRONT
        self._move_arm(position_from_coordinates, rotation={"y": -90, "x": 0, "z": 0})

        # lower hand 11cm
        position_from_coordinates[2] -= 0.11
        self._move_arm(position_from_coordinates, rotation={"y": -90, "x": 0, "z": 0})

        # open hand for taking block
        self.grip_open()
        # Add the constant distance (to the front)
        position_from_coordinates[0] += constants.DELTA_FRONT
        position_from_coordinates[
            0
        ] += 0.02  # move 2 cm further to the front to have the block being safe within the hand
        self._move_arm(position_from_coordinates, rotation={"y": -90, "x": 0, "z": 0})

        # Takes Block
        self.grip_close()

        # raise hand 10cm
        position_from_coordinates[2] += 0.1
        self._move_arm(position_from_coordinates, rotation={"y": -90, "x": 0, "z": 0})

        # beginning of pos_to
        # Add safe height to pos_to coordinates and move to pos_to
        position_to_coordinates[2] += constants.DELTA_HEIGHT
        self._move_arm(
            position_to_coordinates,
            rotation={
                "y": -90,
                "x": 0,
                "z": self.mapper.get_hand_rotation(position_to),
            },
        )

        # Subtract safe height from pos_to
        position_to_coordinates[2] -= constants.DELTA_HEIGHT
        # tilt hand 70 degrees down to not touch other blocks
        self._move_arm(
            position_to_coordinates,
            rotation={
                "y": -70,
                "x": 0,
                "z": self.mapper.get_hand_rotation(position_to),
            },
        )

        # Open Grip to release block
        self.grip_open()

        # Add height
        position_to_coordinates[2] += constants.DELTA_HEIGHT
        self._move_arm(
            position_to_coordinates,
            rotation={
                "y": -90,
                "x": 0,
                "z": self.mapper.get_hand_rotation(position_to),
            },
        )

        # Close grip and move back to waiting position above block 5
        self.grip_close()
        self._move_arm(point_above_Block_5, rotation={"y": -90, "x": 0, "z": 0})

        # move is finished, reachy looks down and turns off his head
        self.move_finished = True
        self.move_head(constants.HEAD_LOOK_DOWN)
        self.reachy.turn_off_smoothly("head")

    def head_follows_arm(self):
        """
        Der Kopf folgt der Hand fortlaufend, bis die Bewegung eines Blocks abgeschlossen ist.
        Diese Funktion muss als Thread innerhalb der `move_object`-Methode aufgerufen werden.
        Die `move_object`-Methode muss die Variable `move_finished` auf True setzen, um die Funktion zu beenden.
        """
        self.move_head()
        time.sleep(0.5)
        while True:
            self.move_head()
            # time.sleep(0.5)
            if self.move_finished:
                sys.exit()

    def head_follows_arm_v2(self, thread_moving_object: Thread):
        """
        Der Kopf folgt der Hand fortlaufend, bis die Bewegung eines Blocks abgeschlossen ist.
        Diese Funktion muss neben der `move_object`-Methode in einem parallelen Thread aufgerufen werden.
        Beendet sich, wenn der Thread `thread_moving_object` beendet ist.
        """
        self.move_head()
        time.sleep(0.5)
        while thread_moving_object.is_alive():
            self.move_head()

    def start_move_object_as_threads(self, pos_from: list, pos_to: Board):
        """
        Diese Funktion versucht, die Kopfbewegung parallel zur Armbewegung auszuführen.
        Sie nutzt auch die Erkennung unbenutzter Blöcke.

        :param pos_from: Die Ausgangsposition des Objekts.
        :param pos_to: Die Zielposition des Objekts.
        """
        thread_moving_object = Thread(target=self.move_object, args=(pos_from, pos_to))
        thread_head_following_hand = Thread(
            target=self.head_follows_arm_v2, args=[thread_moving_object]
        )

        thread_moving_object.start()
        thread_head_following_hand.start()

        while thread_moving_object.is_alive() or thread_head_following_hand.is_alive():
            pass
        print("Movement threads have ended")

    def detecting_nearest_block(self):
        """
        Bewegt den Arm außerhalb des Sichtfelds und erkennt den nächstgelegenen unbenutzten Block.

        :return: Die erkannte Position des nächstgelegenen unbenutzten Blocks.
        """
        self.set_arm_to_side_position()  # Temporary Position to move Arm out of the view
        while True:
            try:
                pos_from = (
                    self.perception.get_nearest_unused_piece()
                )  # returns list [x,y] coord
                pos_from += [
                    -0.05
                ]  # Adds [z] coordinate; Value Adjusted to `Outside.py`
                print("Detected nearest Block with Coordinate:", pos_from)
                ## Adjustments if needed
                # pos_from[0] += 0.00
                # pos_from[1] -= 0.02
                # print("Adjusted Coordinate:", pos_from)

                # Check if the return values are within the desired range
                if -35 <= pos_from[0] <= 35 and -35 <= pos_from[1] <= 35:
                    break
                else:
                    print("The detected Coordinate are outside of desired range")
            except Exception as exeption:
                print(exeption)
                print("Could not detect an unused block")
                # print("Uses Coordinates of Predefined Block 1 instead")
                # pos_from = Outside.BLOCK_1.value
            print("Restarting Detection")
        self.go_to_pos_above_5()  # Returns arm to a Position above Block 5
        return pos_from

    def _move_arm(self, pos_to: list, rotation: dict):
        """
        Bewegt den Arm in die angegebene Position.

        :param pos_to: Die Zielposition des Arms.
        :param rotation: Die Rotationswerte für den Arm.
        """
        duration = self.calculate_dynamic_duration(pos_to)
        target_kinematic = self.kinematic_model_helper.get_kinematic_move(
            pose=pos_to, rotation=rotation
        )
        joint_pos_A = self.reachy.r_arm.inverse_kinematics(target_kinematic)
        goto(
            {
                joint: pos
                for joint, pos in zip(self.reachy.r_arm.joints.values(), joint_pos_A)
            },
            duration + 0.5,
            interpolation_mode=InterpolationMode.MINIMUM_JERK,
        )

    def _change_grip_force(self, force):
        self.POS_GRIPPER[self.reachy.r_arm.r_gripper] = force
        # print("current force:", self.POS_GRIPPER[self.reachy.r_arm.r_gripper])

    def grip_open(self):
        self._change_grip_force(constants.GRIPPER_OPEN_FULL)
        goto(
            goal_positions=self.POS_GRIPPER,
            duration=1.0,
            interpolation_mode=InterpolationMode.MINIMUM_JERK,
        )

    def grip_close(self):
        """
        Schließt den Greifer, bis er etwas hält.
        """
        self._change_grip_force(constants.GRIPPER_CLOSED)
        goto(
            goal_positions=self.POS_GRIPPER,
            duration=1.0,
            interpolation_mode=InterpolationMode.MINIMUM_JERK,
        )

    def _is_holding(self):
        """
        :returns: 'True' if reachy`s right arm is holding something
        """
        # ERROR: force sensors gives too high values (> 10000); but code is equal to official
        # reachy documentation
        if (
            self.reachy.force_sensors.r_force_gripper.force
            > constants.GRIP_FORCE_HOLDING
        ):
            # TODO: Warning when to much Force is applied
            return True
        return False

    def move_body(self, x, y):
        """
        Bewegt den Körper des Reachy/Roboters zu den angegebenen Koordinaten.
        ! Hindernisse werden ignoriert/undefiniert

        :param x: X-Koordinate
        :param y: Y-Koordinate
        """
        self.reachy.mobile_base.goto(x, y, theta=0)

    def turn_body(self, degree):
        """
        Dreht die mobile Basis um den angegebenen Winkel (gegen den Uhrzeigersinn).

        :param degree: Der zu drehende Winkel
        """
        self.reachy.mobile_base.goto(x=0.0, y=0.0, theta=degree)

    def calibrate(self):
        """
        Kalibriert den Ursprungspunkt des Reachy/Roboters und setzt den Ursprungspunkt auf den
        unteren rechten Eckpunkt des Koordinatensystems.

        """
        matrix = self.reachy.r_arm.forward_kinematics()
        x = round(matrix[0][3], 2)
        y = round(matrix[1][3], 2)
        z = -0.37
        res = [x, y, z]
        self.set_origin(res)
        print("Calibration of bottem right corner: ", self.get_origin())

    def move_head(self, look_at=None):
        """
        Bewegt den Kopf des Reachy/Roboters entweder zu den angegebenen Koordinaten (definiert durch look_at) oder
        folgt den Koordinaten des rechten Arms mit Verzögerung.

        :param look_at: Die zu betrachtenden x-, y- und z-Koordinaten
        """
        # Head follows arm
        if look_at is None:
            x, y, z = self.reachy.r_arm.forward_kinematics()[:3, -1]
            self.reachy.head.look_at(x=x, y=y, z=z - 0.05, duration=0.1)
        # Head looks at given x,y,z
        else:
            x, y, z = look_at
            self.reachy.head.look_at(x=x, y=y, z=z, duration=1.0)

    def perform_animation(self, animation_type: Animation, use_sound: bool):
        """
        Führt die angegebene Animation auf dem Reachy/Roboter aus.

        :param animation_type: Der Typ der Animation
        """
        match animation_type:
            case Animation.WIN:
                animation_win(self.reachy, use_sound)
            case Animation.LOSE:
                animation_lose(self.reachy, use_sound)
            case Animation.ANGRY:
                animation_angry(self.reachy, use_sound)
            case Animation.THINKING:
                animation_thinking(self.reachy, use_sound)
            case Animation.DISAPPROVAL:
                animation_disapproval(self.reachy, use_sound)
            case Animation.SAD_ANTENNAS:
                animation_sad_antennas(self.reachy)
            case Animation.HAPPY_ANTENNAS:
                animation_happy_antennas(self.reachy)
            case Animation.LEVEL0:
                animation_level0(self.reachy)
            case Animation.LEVEL1:
                animation_level1(self.reachy)
            case Animation.LEVEL2:
                animation_level2(self.reachy)
            case Animation.LEVEL3:
                animation_level3(self.reachy)
            case Animation.TIE:
                animation_tie(self.reachy, use_sound)
            case Animation.START_REACHY:
                animation_start_reachy(self.reachy, use_sound)
            case Animation.START_OPPONENT:
                animation_start_opponent(self.reachy, use_sound)
            case Animation.FORWARD:
                animation_forward(self.reachy)
            case Animation.CLUELESS:
                animation_clueless(self.reachy)
            case Animation.HAPPY:
                animation_happy(self.reachy)

    def steal_object(self, block: Board):
        """
        Entfernt ein Objekt von einem Block und stiehlt es mit dem linken Arm.

        :param block: Der zu stehlende Block
        """
        self.reachy.turn_on("l_arm")

        self._move_l_arm([0.1, 0.4, 0.05])
        self._open_l_gripper()
        pieces, g_pieces = self.perception.get_already_placed_pieces_coordinates()
        # print(pieces)
        piece = None
        offset_x = 0
        offset_y = 0
        match block:
            case Board.BOTTOM_LEFT:
                piece = pieces[6]
                offset_x = -0.06
            case Board.CENTER_LEFT:
                piece = pieces[3]
            case Board.TOP_LEFT:
                piece = pieces[0]
                offset_y = -0.04

        x = piece[1] / -100
        y = piece[0] / -100
        print("x:", x, "y:", y)
        self._move_l_arm([x - 0.1, y + 0.05, 0])
        self._move_l_arm([x - offset_x, y + offset_y, 0])
        self._close_l_gripper()
        self._move_l_arm([x - 0.06, y, 0.09])

        self._move_l_arm(add_lists(constants.STEAL_PLACE, [0, 0, 0.1]))
        self._move_l_arm(constants.STEAL_PLACE, duration=0.5)
        self._open_l_gripper()
        self._move_l_arm(add_lists(constants.STEAL_PLACE, [0, 0, 0.05]), duration=0.75)
        self._move_l_arm(
            add_lists(constants.STEAL_PLACE, [-0.04, 0, 0.04]), duration=0.75
        )
        self._move_l_arm([-0.03, 0.45, 0.02])

    def _move_l_arm(self, pos, rot=None, duration=None):
        if rot is None:
            rot = {"x": 0, "y": -90, "z": -90}
        if duration is None:
            duration = 1.5
        pos = add_lists(pos, self.get_origin())
        m_target_kinematic = self.kinematic_model_helper.get_kinematic_move(pos, rot)
        m_pos = self.reachy.l_arm.inverse_kinematics(m_target_kinematic)
        goto(
            {joint: p for joint, p in zip(self.reachy.l_arm.joints.values(), m_pos)},
            duration,
        )

    def _close_l_gripper(self):
        goto({self.reachy.l_arm.l_gripper: constants.L_GRIPPER_CLOSE}, duration=1)

    def _open_l_gripper(self):
        goto({self.reachy.l_arm.l_gripper: constants.L_GRIPPER_OPEN}, duration=1)

    def calculate_dynamic_duration(self, pos_to):
        matrix = self.reachy.r_arm.forward_kinematics()
        x = round(matrix[0][3], 2)
        y = round(matrix[1][3], 2)
        z = -0.37
        pos_from = add_lists([x, y, z], self.get_origin())
        res = sub_lists(pos_to, pos_from)
        distance = sqrt(pow(res[0], 2) + pow(res[1], 2) + pow(res[2], 2))
        return distance * constants.ARM_SPEED_FACTOR
