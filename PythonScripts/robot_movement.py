import constants 
from reachy_sdk import ReachySDK
from reachy_sdk.trajectory import goto
from reachy_sdk.trajectory.interpolation import InterpolationMode
# Docs:
# https://docs.pollen-robotics.com/sdk/first-moves/kinematics/#forward-kinematics
# Older Docs (Content may be depricated):
# https://pollen-robotics.github.io/reachy-2019-docs/docs/program-your-robot/control-the-arm/#forward-kinematics

# Instantiate reachy instance
reachy = ReachySDK(host=constants.HOSTADDRESS)

"""
Accessed by '__grip_close()' and '_grip_open()' 
-> Closing until is_holding() == True to not put to much pressure on object
TODO: There is definitly a more elegant Solution :)
"""
gripper_number = 0
POS_GRIPPER = {
    reachy.r_arm.r_gripper: gripper_number,
}

# TODO: Somehow putting these into constants.py - Problem beeing 'reachy'
POS_BASE = {
    reachy.r_arm.r_shoulder_pitch: 0,
    reachy.r_arm.r_shoulder_roll: 0,
    reachy.r_arm.r_arm_yaw: 0,
    reachy.r_arm.r_elbow_pitch: -90,
    reachy.r_arm.r_forearm_yaw: 0,
    reachy.r_arm.r_wrist_pitch: 0,
    reachy.r_arm.r_wrist_roll: 0,
    reachy.r_arm.r_gripper: 0,
}

POS_ABOVE_BOARD = {
    reachy.r_arm.r_shoulder_pitch: 0,
    reachy.r_arm.r_shoulder_roll: 0,
    reachy.r_arm.r_arm_yaw: 0,
    reachy.r_arm.r_elbow_pitch: -90,
    reachy.r_arm.r_forearm_yaw: 0,
    reachy.r_arm.r_wrist_pitch: 0,
    reachy.r_arm.r_wrist_roll: 0,
}



class RobotMovement:
    def __init__(self, reachy):
        self.reachy = reachy

    def move_object(self, pos_from, pos_to):
        """
        Moves Object from A (pos_from) to B (pos_to)

        :param pos_from (array): Coordinates where the Object to move is
        :param pos_to (array): Coordinates on where to move the object
        """

        # 1. Moves arm in front of the Object
        # 2. Opens Hand
        # 3. Moves Hand/arm to the object
        # 4. closes Hand
        # 5. Moves arm above Board
        # 6. moves arm to pos_to
        # 7. opens Hand
        # 8. Moves arm up
        # 9. Moves arm back to Base Position

        self._move_arm()
        pass

    def _move_arm(self, pos_to):
        """
        Moving arm to Position

        """
        pass
    
    def _grip_open(self):
        """
        opens grip until is_holding is false
        """
        pass

    def _grip_close(self):
        """
        closes grip until is_holding is true
        """
        pass

    def _is_holding(self):
        """
        :returns: 'True' if Reachys right arm is holding something
        """
        if abs(reachy.force_sensors.r_force_gripper.force) > constants.GRIP_FORCE_HOLDING:
            # TODO: Warning when to much Force is applied
            return True
        else:
            return False
    
    def move_body(self, pos_to):
        """
        Moves the Reachy/Robot Body to given Coordinates
        !Obstacles are ignored/Undefined

        :param pos_to (array): Coordinates on where to move the object
        """
        pass

    def get_position():
        """
        Returns current Cartesian coordinitas Position

        :param pos_current array: Coordinates - based on origin Point.
        :return: array
        """
        pass




robot = RobotMovement(reachy)


