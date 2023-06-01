import time

from reachy_sdk.trajectory import goto
from reachy_sdk.trajectory.interpolation import InterpolationMode


def animation_angry(reachy):
    """
    pushes cylinders and cubes of the board
    """
    
    reachy.turn_on("r_arm")
    reachy.head.l_antenna.speed_limit = 50.0
    reachy.head.r_antenna.speed_limit = 50.0 
    reachy.head.look_at(0.5, -0.4, -0.4, duration=0.5)
    time.sleep(1.0)
    reachy.head.l_antenna.goal_position = -90
    reachy.head.r_antenna.goal_position = 90

    time.sleep(1.0)
    
    reachy.head.l_antenna.goal_position = -90
    reachy.head.r_antenna.goal_position = 90

    time.sleep(0.5)

    r1_position = {
        reachy.r_arm.r_shoulder_pitch: -15,
        reachy.r_arm.r_shoulder_roll: -50,   # moves left to right
        reachy.r_arm.r_arm_yaw: 35,    # forward/back
        reachy.r_arm.r_elbow_pitch: -75,
        reachy.r_arm.r_forearm_yaw: 0,
        reachy.r_arm.r_wrist_pitch: -10,
        reachy.r_arm.r_wrist_roll: 0,
        reachy.r_arm.r_gripper: 20,
        }
    goto(
        goal_positions=r1_position,
        duration=1.0,
        interpolation_mode=InterpolationMode.MINIMUM_JERK
        )
    r2_position = {
        reachy.r_arm.r_shoulder_pitch: -25, #up / down if too high try -25/-20
        reachy.r_arm.r_shoulder_roll: 0,  # moves left to right
        reachy.r_arm.r_arm_yaw: 40,
        reachy.r_arm.r_elbow_pitch: -50,
        reachy.r_arm.r_forearm_yaw: 0,
        reachy.r_arm.r_wrist_pitch: -10,
        reachy.r_arm.r_wrist_roll: 0,
        reachy.r_arm.r_gripper: 20,
        }
    goto(
        goal_positions=r2_position,
        duration=0.70,
        interpolation_mode=InterpolationMode.MINIMUM_JERK
        )

    rbase_position = {
        reachy.r_arm.r_shoulder_pitch: -15,
        reachy.r_arm.r_shoulder_roll: -45,    # moves left to right
        reachy.r_arm.r_arm_yaw: 35,    # forward/back
        reachy.r_arm.r_elbow_pitch: -75,
        reachy.r_arm.r_forearm_yaw: 0,
        reachy.r_arm.r_wrist_pitch: -25,
        reachy.r_arm.r_wrist_roll: 0,
        reachy.r_arm.r_gripper: 20,
        }
    goto(
        goal_positions=rbase_position,
        duration=0.70,
        interpolation_mode=InterpolationMode.MINIMUM_JERK
        )
    reachy.head.look_at(0.5, -0.1, -0.2, duration=0.4)
    reachy.turn_off_smoothly("r_arm")