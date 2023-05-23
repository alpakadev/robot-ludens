import constants
from reachy_sdk import ReachySDK
from reachy_sdk.trajectory import goto
from reachy_sdk.trajectory.interpolation import InterpolationMode
from Helper.KinematicModelHelper import KinematicModelHelper
import numpy as np
import time


# Docs:
# https://docs.pollen-robotics.com/sdk/first-moves/kinematics/#forward-kinematics
# Older Docs (Content may be depricated):
# https://pollen-robotics.github.io/reachy-2019-docs/docs/program-your-robot/control-the-arm/#forward-kinematics

class MoveImpl:

    def __init__(self, reachy: ReachySDK):
        self.reachy = reachy
        self.kinematic_model_helper = KinematicModelHelper()
        # Starting movement to Base Position
        # self._move_arm(constants.POS_BASE_COORDINATES)
        # Defines Dictionary for modifying the gripping force
        self.POS_GRIPPER = {self.reachy.r_arm.r_gripper: 0}

    def move_object(self, pos_from, pos_to):
        """
        Moves Object from A (pos_from) to B (pos_to)

        :param pos_from: Coordinates where the Object to move is
        :param pos_to: Coordinates on where to move the object
        """
        # Setting arm joints to Stiff-mode for starting movement
        self.reachy.turn_on("r_arm")

        # Tiefe == x (nach vorne), breite == z , Hoehe ==y
        pos_from[1] += constants.DELTA_HAND_WIDTH  # To prevent knocking cylinder on 3.
        # pos_to[1] += constants.DELTA_HAND_WIDTH # To better place into position on 6-8.

        # 1. Moves arm in front of the Object
        pos_from[0] -= constants.DELTA_GRIP_OBJ
        self._move_arm(pos_from)
        pos_from[0] += constants.DELTA_GRIP_OBJ
        # pos_from[0] += constants.DELTA_HAND_TIP # or Else its just the Tip around the cylinder

        # 2. Opens Hand
        self._grip_open()
        # 3. Moves Hand/arm to the object
        self._move_arm(pos_from)
        # 4. closes Hand
        self._grip_close()
        # 5. Moves arm above current position
        pos_from[2] += constants.DELTA_ABOVE_OBJ
        self._move_arm(pos_from)
        pos_from[2] -= constants.DELTA_ABOVE_OBJ
        # 6. Moves arm above pos_to
        pos_to[2] += constants.DELTA_ABOVE_OBJ
        self._move_arm(pos_to)  ##TODO: How to Handle POS_ABOVE_BOARD?
        pos_to[2] -= constants.DELTA_ABOVE_OBJ
        # 7. moves arm to pos_to
        self._move_arm(pos_to)
        # 8. opens Hand
        self._grip_open()
        # 9. Moves arm up
        pos_to[2] += constants.DELTA_ABOVE_OBJ
        self._move_arm(pos_to)
        pos_to[2] -= constants.DELTA_ABOVE_OBJ
        # 10. Moves arm back to Base Position
        self._grip_close()
        self._move_arm(constants.POS_BASE_COORDINATES)  ##TODO: How to Handle POS_BASE?

        # Setting arm to compliant mode and lowering smoothly for preventing damaging
        self.reachy.turn_off_smoothly("r_arm")
        pass

    def _move_arm(self, pos_to):
        """
        Moving arm to Position

        """
        print(pos_to)
        # Only adjust the rot_direction [x, y, z] and the rot_axis of type deg and then the arm movement
        # should be precise
        target_kinematic = self.kinematic_model_helper.get_kinematic_move(pose=pos_to, rot_direction='y', rot_axis=-90)

        joint_pos_A = self.reachy.r_arm.inverse_kinematics(target_kinematic)
        goto({joint: pos for joint, pos in zip(self.reachy.r_arm.joints.values(), joint_pos_A)}, duration=2.0)
        pass

    def _change_grip_force(self, force):
        self.POS_GRIPPER[self.reachy.r_arm.r_gripper] = force
        print("current force:", self.POS_GRIPPER[self.reachy.r_arm.r_gripper])
        pass

    def _grip_open(self):
        """
        opens grip completly
        """
        # Open grip completly
        self._change_grip_force(-60)
        goto(goal_positions=self.POS_GRIPPER, duration=1.0, interpolation_mode=InterpolationMode.MINIMUM_JERK)
        pass

    def _grip_close(self):
        """
        closes grip until is_holding is true
        """
        # Closes grip
        # TODO: CLOSE until _is_holding
        self._change_grip_force(5)
        goto(goal_positions=self.POS_GRIPPER, duration=1.0, interpolation_mode=InterpolationMode.MINIMUM_JERK)
        pass

    def _is_holding(self):
        """
        :returns: 'True' if Reachys right arm is holding something
        """
        if abs(self.reachy.force_sensors.r_force_gripper.force) > constants.GRIP_FORCE_HOLDING:
            # TODO: Warning when to much Force is applied
            return True
        else:
            return False

    def _prepare_body_movement(self):
        # bring arms in safe position
        self._move_arm(constants.POS_SAVE_COORDINATES)
        pass

    def _finish_body_movement(self):
        self._move_arm(constants.POS_BASE_COORDINATES)
        pass

    def move_body(self, x, y):
        """
        Moves the Reachy/Robot Body to given Coordinates
        !Obstacles are ignored/Undefined

        :param pos_to (array): Coordinates on where to move the object
        """
        self._prepare_body_movement()
        self.reachy.mobile_base.goto(x,y, theta=0)
        self._finish_body_movement()

    def turn_body(self, degree):
        """
        Rotates the mobile base by a given angle (counterclockwise)
        :param degree: The angle to rotate
        """
        self._prepare_body_movement()
        time.sleep(2)
        self.reachy.mobile_base.goto(x=0.0, y=0.0, theta=degree)
        time.sleep(2)
        self._finish_body_movement()

    def get_position(self):
        """
        Returns current Cartesian coordinitas Position

        :param pos_current array: Coordinates - based on origin Point.
        :return: array
        """
        pass


if __name__ == "__main__":
    # Instantiate reachy instance
    reachy_sdk = ReachySDK(host=constants.HOSTADDRESS, with_mobile_base=True)

    robot = MoveImpl(reachy_sdk)
    reachy_sdk.turn_on("reachy")

    # [depth, width, height]
    # Unity: depth(front) == -x , width(side) == -z , height() == y
    pos_cylinder = [0.4, -0.3, -0.38]
    pos_goal = [0.4, 0, -0.38]

    robot.turn_body(180)
    reachy_sdk.turn_off_smoothly("reachy")

