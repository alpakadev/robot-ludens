import constants 
from reachy_sdk import ReachySDK
from reachy_sdk.trajectory import goto
from reachy_sdk.trajectory.interpolation import InterpolationMode

HOSTADRESS = 'localhost'

# TODO: Calculate the path that the robot arm needs to follow to move the object from point a to point b. 
# Use Inverse kinematics, forward kinematics, or motion planning algorithms.
# https://docs.pollen-robotics.com/sdk/first-moves/kinematics/#forward-kinematics
# Older Docs (Content may be depricated):
# https://pollen-robotics.github.io/reachy-2019-docs/docs/program-your-robot/control-the-arm/#forward-kinematics

# forward kinematics: joint coordinates –> cartesian coordinates,
# inverse kinematics: cartesian coordinates –> joint coordinates.
# 'right_tip' should be the middle of Reachys Hand

class RobotMovement:
    def __init__(self, reachy):
        self.reachy = reachy
    
    # Actuall movement of arms to Cartesian Coordinates
    def move_to_position(self, position):
        pass
    
    # Movement
    # pos_from , pos_to beeing the TicTacToe fields
    def move_object_to(self, pos_from, pos_to):
        pass

    # Returns current Cartesian coordinitas Position
    def get_position():
        pass

    # returns boolean if Hand is holding something (check grip_force)
    def is_holding():
        if abs(reachy.force_sensors.r_force_gripper.force) < constants.GRIP_FORCE_HOLDING:
            return True
        else:
            return False


# Connect to reachy instance
reachy = ReachySDK(host=constants.HOSTADRESS)
robot = RobotMovement(reachy)


