import time

from reachy_sdk.trajectory import goto
from reachy_sdk.trajectory.interpolation import InterpolationMode
"""
NOT TESTED YET
testing mobile base
reachy in freie fläche!!!
"""
def animation_forward(reachy): #!!!not tested yet!!!!

    reachy.turn_on("r_arm") 
    reachy.turn_on("l_arm")
    
    # safe position arms to move from table 
    right_base_position = {
        reachy.r_arm.r_shoulder_pitch: -50,
        reachy.r_arm.r_shoulder_roll: 0,  # moves left to right
        reachy.r_arm.r_arm_yaw: 0,  # forward/back
        reachy.r_arm.r_elbow_pitch: -140,
        reachy.r_arm.r_forearm_yaw: 0,
        reachy.r_arm.r_wrist_pitch: 0,
        reachy.r_arm.r_wrist_roll: 0,
        reachy.r_arm.r_gripper: 0,
    }
    
    goto(
        goal_positions=right_base_position,
        duration=0.90,
        interpolation_mode=InterpolationMode.MINIMUM_JERK
    )

    left_base_position = {
        reachy.l_arm.l_shoulder_pitch: -50,
        reachy.l_arm.l_shoulder_roll: 0,  # moves left to right
        reachy.l_arm.l_arm_yaw: 0,  # forward/back
        reachy.l_arm.l_elbow_pitch: -140,
        reachy.l_arm.l_forearm_yaw: 0,
        reachy.l_arm.l_wrist_pitch: 0,
        reachy.l_arm.l_wrist_roll: 0,
        reachy.l_arm.l_gripper: 0,
    }
    goto(
        goal_positions=left_base_position,
        duration=0.90,
        interpolation_mode=InterpolationMode.MINIMUM_JERK
    )


   # reachy.mobile.reset_odometry() #resets current posiiton of reachy
  # if you ask for a goto(0, 0, 0) the robot will try to comeback to the position it was at boot-up.
    reachy.mobile_base.goto(x=0.10, y=0.0, theta=0) 
    #x == Front, y == Left in meter,
    #positive theta counterclockwise in degree,...negative theta clockwise (?)