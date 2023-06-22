import time

from reachy_sdk.trajectory import goto
from reachy_sdk.trajectory.interpolation import InterpolationMode

from .HappyAntennas import animation_happy_antennas

def animation_win(reachy):
    reachy.turn_on("head")
    reachy.turn_on("r_arm")
    reachy.turn_on("l_arm")  # stiff mode for l_arm

    reachy.head.look_at(0.5, 0, -0.4, duration=1.0) 

    time.sleep(0.5)

    reachy.head.look_at(0.5, -0, 0, duration=0.5)
    reachy.head.l_antenna.goal_position = 40.0
    reachy.head.r_antenna.goal_position = -40.0
        
    for _ in range(2):

        reachy.head.look_at(0.5, 0, 0.2, duration=0.70) 
        time.sleep(0.1)
        reachy.head.look_at(0.5, 0, -0.2, duration=0.70) 
    reachy.head.look_at(0.5, 0, -0, duration=0.80)
            
    time.sleep(0.2)

    for i in range(3):
        right_up_position = {
            reachy.r_arm.r_shoulder_pitch: -60,
            reachy.r_arm.r_shoulder_roll: 0,
            reachy.r_arm.r_arm_yaw: 0,
            reachy.r_arm.r_elbow_pitch: -120,
            reachy.r_arm.r_forearm_yaw: 0,
            reachy.r_arm.r_wrist_pitch: 0,
            reachy.r_arm.r_wrist_roll: 0,
            reachy.r_arm.r_gripper: 20,
        }
        left_up_position = {
            reachy.l_arm.l_shoulder_pitch: -60,
            reachy.l_arm.l_shoulder_roll: 0,
            reachy.l_arm.l_arm_yaw: 0,
            reachy.l_arm.l_elbow_pitch: -120,
            reachy.l_arm.l_forearm_yaw: 0,
            reachy.l_arm.l_wrist_pitch: 0,
            reachy.l_arm.l_wrist_roll: 0,
            reachy.l_arm.l_gripper: 20,
        }

        
        goto(
            goal_positions=left_up_position,
            duration=0.5,
            interpolation_mode=InterpolationMode.MINIMUM_JERK
        )
        
        goto(
            goal_positions=right_up_position,
            duration=0.3,
            interpolation_mode=InterpolationMode.MINIMUM_JERK
        )
        animation_happy_antennas(reachy)
        reachy.head.look_at(0.3, 0.20, -0.1, duration=0.50)
       

        right_up2_position = {
            reachy.r_arm.r_shoulder_pitch: -80,
            reachy.r_arm.r_shoulder_roll: 0,
            reachy.r_arm.r_arm_yaw: 0,
            reachy.r_arm.r_elbow_pitch: -120,
            reachy.r_arm.r_forearm_yaw: 0,
            reachy.r_arm.r_wrist_pitch: 0,
            reachy.r_arm.r_wrist_roll: 0,
            reachy.r_arm.r_gripper: -20,
        }
        left_up2_position = {
            reachy.l_arm.l_shoulder_pitch: -80,
            reachy.l_arm.l_shoulder_roll: 0,
            reachy.l_arm.l_arm_yaw: 0,
            reachy.l_arm.l_elbow_pitch: -120,
            reachy.l_arm.l_forearm_yaw: 0,
            reachy.l_arm.l_wrist_pitch: 0,
            reachy.l_arm.l_wrist_roll: 0,
            reachy.l_arm.l_gripper: -20,
        }
       
        goto(
            goal_positions=left_up2_position,
            duration=0.3,
            interpolation_mode=InterpolationMode.MINIMUM_JERK
        )
        
        goto(
            goal_positions=right_up2_position,
            duration=0.5,
            interpolation_mode=InterpolationMode.MINIMUM_JERK
        )

        if i == 2:
            reachy.head.look_at(0.5, 0, 0, duration=0.90)
        else:   
            reachy.head.look_at(0.4, -0.2, -0.1, duration=0.50)
    
    #go back to default
    right_base_position = {
        reachy.r_arm.r_shoulder_pitch: -25,
        reachy.r_arm.r_shoulder_roll: -20,  # moves left to right
        reachy.r_arm.r_arm_yaw: 15,  # forward/back
        reachy.r_arm.r_elbow_pitch: -40,
        reachy.r_arm.r_forearm_yaw: -15,
        reachy.r_arm.r_wrist_pitch: -25,
        reachy.r_arm.r_wrist_roll: 0,
        reachy.r_arm.r_gripper: 20,
    }
    left_base_position = {
        reachy.l_arm.l_shoulder_pitch: -25,
        reachy.l_arm.l_shoulder_roll: -20,  # moves left to right
        reachy.l_arm.l_arm_yaw: 15,  # forward/back
        reachy.l_arm.l_elbow_pitch: -40,
        reachy.l_arm.l_forearm_yaw: -15,
        reachy.l_arm.l_wrist_pitch: -25,
        reachy.l_arm.l_wrist_roll: 0,
        reachy.l_arm.l_gripper: 20,
    }
    goto(
        goal_positions=right_base_position,
        duration=0.90,
        interpolation_mode=InterpolationMode.MINIMUM_JERK
    )
    goto(
        goal_positions=left_base_position,
        duration=0.90,
        interpolation_mode=InterpolationMode.MINIMUM_JERK
    )
    reachy.head.look_at(0.5, -0, 0, duration=0.5)
    reachy.turn_off_smoothly("l_arm")
    reachy.turn_off_smoothly("r_arm")
    reachy.turn_off("head")
