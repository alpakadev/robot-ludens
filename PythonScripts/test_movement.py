import constants
from reachy_sdk import ReachySDK
from reachy_sdk.trajectory import goto
from reachy_sdk.trajectory.interpolation import InterpolationMode
from scipy.spatial.transform import Rotation as R
import numpy as np
import time

# This is a test file for programming linearly

# connecting to reachy
reachy = ReachySDK(host=constants.HOSTADRESS)

# TODO: This should be in `constants.py`; Problem: Reachy is not yet defined there.
POS_BASE2 = {
    reachy.r_arm.r_shoulder_pitch: 0,
    reachy.r_arm.r_shoulder_roll: 0,
    reachy.r_arm.r_arm_yaw: 0,
    reachy.r_arm.r_elbow_pitch: -90,
    reachy.r_arm.r_forearm_yaw: 0,
    reachy.r_arm.r_wrist_pitch: 0,
    reachy.r_arm.r_wrist_roll: 0,
}

reachy.turn_on("r_arm")
# go to Base Position
goto(
    goal_positions=POS_BASE2,
    duration=1.0,
    interpolation_mode=InterpolationMode.MINIMUM_JERK
)
reachy.turn_off("r_arm")

# forward kinematics: joint coordinates –> cartesian coordinates,

# print(reachy.r_arm.forward_kinematics()) # returns a non-rounded position matrix
# The 4th column gives information about coordinates in room
print(reachy.r_arm.forward_kinematics(joints_position=[0, 0, 0, 0, 0, 0, 0])) # returns a rounded position matrix

# Calculates rotation of the specific given Position matrix.
# Here: Calculating the (Hand) Rotation of POS_BASE -> [0,0,0]
calc_cordinates = R.from_matrix([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1],
    ]).as_euler('xyz', degrees=True)
print(calc_cordinates) 

# in old docs: reachy.right_arm.hand.grip_force
if abs(reachy.force_sensors.r_force_gripper.force) < constants.GRIP_FORCE_HOLDING:
    print('not holding')
else:
    print('holding')

# inverse kinematics: cartesian coordinates –> joint coordinates.

# text from Docs:
# But having the 3D position is not enough to design a pose. 
# You also need to provide the 3D orientation via a rotation matrix. 
# The rotation matrix is often the tricky part when building a target pose matrix.

# TODO: Try the 4 position from the Docs: https://docs.pollen-robotics.com/sdk/first-moves/kinematics/#defining-the-poses
# A = (0.3, -0.4, -0.3)
# B = (0.3, -0.4, 0.0)
# C = (0.3, -0.1, 0.0)
# D = (0.3, -0.1, -0.3)

# Copied from Docs above
A = np.array([
  [0, 0, -1, 0.3],
  [0, 1, 0, -0.4],  
  [1, 0, 0, -0.3],
  [0, 0, 0, 1],  
])

B = np.array([
  [0, 0, -1, 0.3],
  [0, 1, 0, -0.4],  
  [1, 0, 0, 0.0],
  [0, 0, 0, 1],  
])

C = np.array([
  [0, 0, -1, 0.3],
  [0, 1, 0, -0.1],  
  [1, 0, 0, 0.0],
  [0, 0, 0, 1],  
])

D = np.array([
  [0, 0, -1, 0.3],
  [0, 1, 0, -0.1],  
  [1, 0, 0, -0.3],
  [0, 0, 0, 1],  
])

joint_pos_A = reachy.r_arm.inverse_kinematics(A)
joint_pos_B = reachy.r_arm.inverse_kinematics(B)
joint_pos_C = reachy.r_arm.inverse_kinematics(C)
joint_pos_D = reachy.r_arm.inverse_kinematics(D)

# put the joints in stiff mode
reachy.turn_on('r_arm')

# use the goto function
goto({joint: pos for joint,pos in zip(reachy.r_arm.joints.values(), joint_pos_A)}, duration=1.0)
time.sleep(0.5)
goto({joint: pos for joint,pos in zip(reachy.r_arm.joints.values(), joint_pos_B)}, duration=1.0)
time.sleep(0.5)
goto({joint: pos for joint,pos in zip(reachy.r_arm.joints.values(), joint_pos_C)}, duration=1.0)
time.sleep(0.5)
goto({joint: pos for joint,pos in zip(reachy.r_arm.joints.values(), joint_pos_D)}, duration=1.0)

# put the joints back to compliant mode
# use turn_off_smoothly to prevent the arm from falling hard
reachy.turn_off_smoothly('r_arm')