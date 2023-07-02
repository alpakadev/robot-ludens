import time
from reachy_sdk.trajectory import goto
from reachy_sdk.trajectory.interpolation import InterpolationMode
from .HappyAntennas import animation_happy_antennas

def animation_start_reachy(reachy):
    
    reachy.turn_on("l_arm")
    reachy.turn_on("head")
    
    reachy.head.l_antenna.speed_limit = 40.0
    reachy.head.r_antenna.speed_limit = 40.0

    reachy.head.l_antenna.goal_position = 50.0
    reachy.head.r_antenna.goal_position = -30.0
    
    l_arm = {
        reachy.l_arm.l_shoulder_pitch: -25, #up or down
        reachy.l_arm.l_shoulder_roll: 0,   # moves left to right
        reachy.l_arm.l_arm_yaw: 0,    # forward/back
        reachy.l_arm.l_elbow_pitch: -140,
        reachy.l_arm.l_forearm_yaw: 20,
        reachy.l_arm.l_wrist_pitch: -20,
        reachy.l_arm.l_wrist_roll: 0,
        reachy.l_arm.l_gripper: -40,
        }
    
    goto(
        goal_positions=l_arm,
        duration = 0.8,
        interpolation_mode=InterpolationMode.MINIMUM_JERK
        )
    
    
    reachy.head.look_at(0.5, 0.1, -0.05, 1)
    time.sleep(0.2)

    
    l_arm3 = {
        reachy.l_arm.l_shoulder_pitch: -20,
        reachy.l_arm.l_shoulder_roll: 5,   # moves left to right
        reachy.l_arm.l_arm_yaw: -40,    # forward/back
        reachy.l_arm.l_elbow_pitch: -140,
        reachy.l_arm.l_forearm_yaw: 30,
        reachy.l_arm.l_wrist_pitch: -20,
        reachy.l_arm.l_wrist_roll: 0,
        reachy.l_arm.l_gripper: -45,
        }
    
    goto(
        goal_positions=l_arm3,
        duration = 0.8,
        interpolation_mode=InterpolationMode.MINIMUM_JERK
        )
    reachy.head.look_at(0.5, 0, -0.15, 1)

    for _ in range(2):
        
        l_point = {
        reachy.l_arm.l_shoulder_pitch: -20,
        reachy.l_arm.l_shoulder_roll: 5,   # moves left to right
        reachy.l_arm.l_arm_yaw: -40,    # forward/back
        reachy.l_arm.l_elbow_pitch: -140,
        reachy.l_arm.l_forearm_yaw: 30,
        reachy.l_arm.l_wrist_pitch: -25,
        reachy.l_arm.l_wrist_roll: 0,
        reachy.l_arm.l_gripper: -35,
        }
    
        goto(
            goal_positions=l_point,
            duration = 1.0,
            interpolation_mode=InterpolationMode.MINIMUM_JERK
            )
        
        l_point2 = {
        reachy.l_arm.l_shoulder_pitch: -27,
        reachy.l_arm.l_shoulder_roll: 10,   # moves left to right
        reachy.l_arm.l_arm_yaw: -47,    # forward/back
        reachy.l_arm.l_elbow_pitch: -130,
        reachy.l_arm.l_forearm_yaw: 35,
        reachy.l_arm.l_wrist_pitch: -10,
        reachy.l_arm.l_wrist_roll: -15,
        reachy.l_arm.l_gripper: -45,
        }

        animation_happy_antennas(reachy)

        goto(
            goal_positions=l_point2,
            duration = 1.0,
            interpolation_mode=InterpolationMode.MINIMUM_JERK
            )
        
    left_base_position = {
        reachy.l_arm.l_shoulder_pitch: -25,
        reachy.l_arm.l_shoulder_roll: 0,  # moves left to right
        reachy.l_arm.l_arm_yaw: 15,  # forward/back
        reachy.l_arm.l_elbow_pitch: -40,
        reachy.l_arm.l_forearm_yaw: -15,
        reachy.l_arm.l_wrist_pitch: -25,
        reachy.l_arm.l_wrist_roll: 0,
        reachy.l_arm.l_gripper: -45,
    }
    goto(
        goal_positions=left_base_position,
        duration=1.0,
        interpolation_mode=InterpolationMode.MINIMUM_JERK
    )

    reachy.head.l_antenna.goal_position = 0.0
    reachy.head.r_antenna.goal_position = 0.0
    reachy.head.look_at(0.5, 0, 0, 1)
    reachy.turn_off_smoothly("l_arm")
  
   