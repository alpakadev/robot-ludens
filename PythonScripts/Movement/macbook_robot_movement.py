import constants
from reachy_sdk import ReachySDK
from reachy_sdk.trajectory import goto
from reachy_sdk.trajectory.interpolation import InterpolationMode
import numpy as np
import time

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
POS_GRIPPER_OPEN = {
    reachy.r_arm.r_gripper: -60,
}

POS_GRIPPER_CLOSED = {
    reachy.r_arm.r_gripper: 0,
}

"""
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
"""

POS_BASE_COORDINATES = [0.36, -0.20, -0.25]
POS_ABOVE_BOARD_COODINATES = [0.40, 0, 0.10] #old: [0.36, 0, 0]




class RobotMovement:
    def __init__(self, reachy):
        self.reachy = reachy
        self._move_arm(POS_BASE_COORDINATES)

    def move_object(self, pos_from, pos_to):
        """
        Moves Object from A (pos_from) to B (pos_to)

        :param pos_from (array): Coordinates where the Object to move is
        :param pos_to (array): Coordinates on where to move the object
        """
        self.move_head()
        # Tiefe == x (nach vorne), breite == z , Hoehe ==y
        pos_from[1] += constants.DELTA_HAND_WIDTH # To prevent knocking cylinder on 3.
        # pos_to[1] += constants.DELTA_HAND_WIDTH # To better place into position on 6-8.
        self.move_head()
        # 1. Moves arm in front of the Object
        pos_from[0] -= constants.DELTA_GRIP_OBJ
        self._move_arm(pos_from)
        pos_from[0] += constants.DELTA_GRIP_OBJ
        # pos_from[0] += constants.DELTA_HAND_TIP # or Else its just the Tip around the cylinder
        self.move_head()
        # 2. Opens Hand
        self._grip_open()
        
        # 3. Moves Hand/arm to the object
        self._move_arm(pos_from)
        self.move_head()
        # 4. closes Hand
        self._grip_close()

        # 5. Moves arm above Board
        self._move_arm(POS_ABOVE_BOARD_COODINATES) ##TODO: How to Handle POS_ABOVE_BOARD?
        self.move_head()

        # 6. moves arm to pos_to
        self._move_arm(pos_to)
        self.move_head()
         #7. opens Hand
        self._grip_open()
         #8. Moves arm up
        pos_to[2] += constants.DELTA_ABOVE_OBJ
        self._move_arm(pos_to)
        self.move_head()
        pos_to[2] -= constants.DELTA_ABOVE_OBJ
         #9. Moves arm back to Base Position
        self._grip_close()
        self._move_arm(POS_BASE_COORDINATES) ##TODO: How to Handle POS_BASE?
        self.move_head()

        pass

    def _move_arm(self, pos_to):
        """
        Moving arm to Position

        """
        print(pos_to)
        #TODO: Moving
        A = np.array([
            [0, 0, -1, pos_to[0]],
            [0, 1, 0, pos_to[1]],  
            [1, 0, 0, pos_to[2]],
            [0, 0, 0, 1],  
        ])
        joint_pos_A = reachy.r_arm.inverse_kinematics(A)
        reachy.turn_on('r_arm')
        goto({joint: pos for joint,pos in zip(reachy.r_arm.joints.values(), joint_pos_A)}, duration=2.0)
        reachy.turn_off('r_arm')
        pass
    
    def _grip_open(self):
        """
        opens grip completly
        """
        #TODO: Open completly
        reachy.turn_on("r_arm")
        goto(goal_positions=POS_GRIPPER_OPEN,duration=1.0,interpolation_mode=InterpolationMode.MINIMUM_JERK)
        reachy.turn_off("r_arm")
        pass

    def _grip_close(self):
        """
        closes grip until is_holding is true
        """
        #TODO: CLOSE until _is_holding
        reachy.turn_on("r_arm")
        goto(goal_positions=POS_GRIPPER_CLOSED,duration=1.0,interpolation_mode=InterpolationMode.MINIMUM_JERK)
        reachy.turn_off("r_arm")
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
    
# head following hand movement
# improve: instead of if a while loop shall be used -> see: https://docs.pollen-robotics.com/sdk/first-moves/head/

    def move_head(self):
        reachy.turn_on('head')
        
        # possible alternative:
        #reachy.head.look_at(x =pos_from[0] , y=pos_from[1] , z=pos_from[2]-0.05, duration = 1.0)
        #reachy.head.look_at(x =pos_to[0] , y=pos_to[1] , z=pos_to[2]-0.05, duration = 1.0)

        # moving specific parts
        #head_tilted_position = {
        #reachy.head.neck_roll: 0,
        #reachy.head.neck_pitch: 0,
        #reachy.head.neck_yaw:0,
        #}
        
        x, y, z = reachy.r_arm.forward_kinematics()[:3,-1] 
        reachy.head.look_at(x=x, y=y, z=z-0.05, duration=1.0) 

        #time.sleep(0.5)

        if True: # instead of if statement a while loop is used in the actual code...
            x, y, z = reachy.r_arm.forward_kinematics()[:3,-1]
            gp_dic = reachy.head._look_at(x, y, z - 0.05)
            reachy.head.neck_roll.goal_position = gp_dic[reachy.head.neck_roll]
            reachy.head.neck_pitch.goal_position = gp_dic[reachy.head.neck_pitch]
            reachy.head.neck_yaw.goal_position = gp_dic[reachy.head.neck_yaw]
            time.sleep(0.01)
            
        reachy.turn_off('head')
        pass





robot = RobotMovement(reachy)

# Tiefe == -x (nach vorne), breite == -z , Hoehe == -y
pos_cylinder = [0.33, -0.37, -0.32]
pos_goal = [0.0, 0,-0.33]



pos_cylinder2 = [0.47, -0.36, -0.30]
pos_goal2 = [0.32, -0.10,-0.32] #2


pos_cylinder3 = [0.33, -0.47, -0.32]
pos_goal3 = [0.49, -0.17,-0.30] #3
 

robot.move_object(pos_cylinder, pos_goal)
robot.move_object(pos_cylinder2, pos_goal2)
robot.move_object(pos_cylinder3, pos_goal3)
