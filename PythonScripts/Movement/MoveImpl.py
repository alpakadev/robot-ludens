import constants
from reachy_sdk import ReachySDK
from reachy_sdk.trajectory import goto
from reachy_sdk.trajectory.interpolation import InterpolationMode
from Helper.KinematicModelHelper import KinematicModelHelper
from Helper.KinematicModelHelper import RotationAxis
import numpy as np
import time
from Enums.Board import Board
from Enums.Outside import Outside
from Helper.HandRotationMapper import HandRotationMapper


# Docs:
# https://docs.pollen-robotics.com/sdk/first-moves/kinematics/#forward-kinematics
# Older Docs (Content may be depricated):
# https://pollen-robotics.github.io/reachy-2019-docs/docs/program-your-robot/control-the-arm/#forward-kinematics

class MoveImpl:
    
    

    def __init__(self, reachy):
        self.reachy = reachy
        self.kinematic_model_helper = KinematicModelHelper()
        # Starting movement to Base Position
        self._move_arm(constants.POS_BASE_COORDINATES, rotation={'y': -90, 'x': 0, 'z': 0})
        # Defines Dictionary for modifying the gripping force
        self.POS_GRIPPER = {self.reachy.r_arm.r_gripper: 0}
        self.basePosition = [0.2, -0.20, -0.38]

    def getBasePos(self):
        return self.basePosition

    def setBasePos(self, coordinate):
        self.basePosition = coordinate
        
    def addlists(self,a,b):
        c = a
        for i in range(len(c)):
            c[i] += b[i]
            return c
            

    def move_object(self, pos_from_enum: Outside, pos_to_enum: Board):
        """
        Moves Object from A (pos_from) to B (pos_to)

        :param pos_from: Coordinates where the Object to move is
        :param pos_to: Coordinates on where to move the object
        """
        mapper = HandRotationMapper()
        # Setting arm joints to Stiff-mode for starting movement
        self.reachy.turn_on("r_arm")
        # Setting head joints to stiff mode
        self.reachy.turn_on("head")

        pos_to_value = pos_to_enum.value
        pos_from_value = pos_from_enum.value

        pos_from_value = self.addlists(self.basePosition, pos_from_value)
        pos_to_value = self.addlists(self.basePosition, pos_to_value)

        # Tiefe == x (nach vorne), breite == z , Hoehe ==y
        pos_from_value[1] += constants.DELTA_HAND_WIDTH  # To prevent knocking cylinder on 3.
        # pos_to[1] += constants.DELTA_HAND_WIDTH # To better place into position on 6-8.
        # starting movement of reachy's head
        self.move_head(constants.HEAD_LOOK_DOWN)
        time.sleep(1.0)
        self.move_head(constants.HEAD_LOOK_AHEAD)
        self.move_head()
        # 1. Moves arm in front of the Object
        pos_from_value[0] -= constants.DELTA_GRIP_OBJ
        self._move_arm(pos_from_value, rotation={'y': -90, 'x': 0, 'z': 0})
        pos_from_value[0] += constants.DELTA_GRIP_OBJ
        # pos_from[0] += constants.DELTA_HAND_TIP # or Else its just the Tip around the cylinder
        self.move_head()
        # 2. Opens Hand
        self._grip_open()
        # 3. Moves Hand/arm to the object
        self._move_arm(pos_from_value, rotation={'y': -90, 'x': 0, 'z': 0})
        # 4. closes Hand
        self._grip_close()
        # 5. Moves arm above current position
        pos_from_value[2] += constants.DELTA_ABOVE_OBJ
        self._move_arm(pos_from_value, rotation={'y': -90, 'x': 0, 'z': 0})
        pos_from_value[2] -= constants.DELTA_ABOVE_OBJ
        #self.move_head(pos_goal)
        # 6. Moves arm above pos_to
        pos_to_value[2] += constants.DELTA_ABOVE_OBJ
        self._move_arm(pos_to_value, rotation={'y': -90, 'x': 0, 'z': mapper.get_hand_rotation(pos_to_enum)})  ##TODO: How to Handle POS_ABOVE_BOARD?
        pos_to_value[2] -= constants.DELTA_ABOVE_OBJ
        self.move_head()
        # 7. moves arm to pos_to
        self._move_arm(pos_to_value, rotation={'y': -90, 'x': 0, 'z': mapper.get_hand_rotation(pos_to_enum)})
        # 8. opens Hand
        self._grip_open()
        # 9. Moves arm up
        pos_to_value[2] += constants.DELTA_ABOVE_OBJ
        self._move_arm(pos_to_value, rotation={'y': -90, 'x': 0, 'z': mapper.get_hand_rotation(pos_to_enum)})
        pos_to_value[2] -= constants.DELTA_ABOVE_OBJ
        self.move_head()
        # 10. Moves arm back to Base Position
        self._grip_close()
        self._move_arm(constants.POS_BASE_COORDINATES, rotation={'y': -90, 'x': 0, 'z': 0})  ##TODO: How to Handle POS_BASE?

        # Setting arm to compliant mode and lowering smoothly for preventing damaging
        self.reachy.turn_off_smoothly("r_arm")
        # head back to default and setting head to compliant mode
        self.move_head(constants.HEAD_LOOK_AHEAD)
        self.reachy.turn_off("head")
        pass

    def _move_arm(self, pos_to: list, rotation: dict):
        """
        Moving arm to Position

        """
        # Only adjust the rot_direction [x, y, z] and the rot_axis of type deg and then the arm movement
        # should be precise
        target_kinematic = self.kinematic_model_helper.get_kinematic_move(pose=pos_to, rotation=rotation)

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

    def move_body(self, pos_to):
        """
        Moves the Reachy/Robot Body to given Coordinates
        !Obstacles are ignored/Undefined

        :param pos_to (array): Coordinates on where to move the object
        """
        pass

    def get_position(self):
        """
        Returns current Cartesian coordinitas Position

        :param pos_current array: Coordinates - based on origin Point.
        :return: array
        """
        pass
    
    def move_head(self, look_at = None):
        """
        Moves reachy's head either by the given coordinates defined by look_at or
        follows the right arm's coordinates 
        
        """
        # head follows arm
        if look_at is None:
            x, y, z = self.reachy.r_arm.forward_kinematics()[:3,-1] 
            self.reachy.head.look_at(x=x, y=y, z=z-0.05, duration=1.0)
            
        # head looks at given x,y,z
        else:
            x,y,z = look_at
            self.reachy.head.look_at(x=x, y=y, z=z, duration=1.0) 


if __name__ == "__main__":
    # Instantiate reachy instance
    reachy_sdk = ReachySDK(host=constants.HOSTADDRESS)

    robot = MoveImpl(reachy_sdk)

    # [depth, width, height]
    # Unity: depth(front) == -x , width(side) == -z , height() == y

    robot.move_object(Outside.BLOCK_1, Board.TOP_RIGHT)
