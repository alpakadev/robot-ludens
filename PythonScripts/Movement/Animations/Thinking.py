import time
import random

from reachy_sdk.trajectory import goto
from reachy_sdk.trajectory.interpolation import InterpolationMode

def animation_thinking(reachy):
    # Scratch head with hand
    reachy.turn_on("head")
    reachy.head.look_at(0.5, -0.3, -0.2, duration=1.0)
    reachy.head.l_antenna.goal_position = 40.0
    reachy.head.r_antenna.goal_position = -80.0
    time.sleep(0.50)

    reachy.turn_on("l_arm")
    degree = random.randint(5, 25)

    for x in range(3):
        degree  += random.randint(15,25)
        left_touch_head_position = {
            reachy.l_arm.l_shoulder_pitch: -65,  # if too far away lower value
            reachy.l_arm.l_shoulder_roll: 10,
            reachy.l_arm.l_arm_yaw: -22,
            reachy.l_arm.l_elbow_pitch: -125,
            reachy.l_arm.l_forearm_yaw: -10,
            reachy.l_arm.l_wrist_pitch: -30,
            reachy.l_arm.l_wrist_roll: 0,
            reachy.l_arm.l_gripper: -40,
        }
        goto(
            goal_positions=left_touch_head_position,
            duration=1.0,
            interpolation_mode=InterpolationMode.MINIMUM_JERK
        )
        time.sleep(0.1)
        print(degree//2)
        reachy.head.l_antenna.speed_limit = 90.0 - degree//2
        reachy.head.r_antenna.speed_limit = 60.0 - degree//2
        reachy.head.l_antenna.goal_position = 50.0 - degree
        reachy.head.r_antenna.goal_position = -90.0 + degree

        time.sleep(0.1)
        left_scratch = {
            reachy.l_arm.l_shoulder_pitch: -60,  # if too far away lower
            reachy.l_arm.l_shoulder_roll: 10,
            reachy.l_arm.l_arm_yaw: -20,
            reachy.l_arm.l_elbow_pitch: -125,
            reachy.l_arm.l_forearm_yaw: -10,
            reachy.l_arm.l_wrist_pitch: 0,
            reachy.l_arm.l_wrist_roll: 0,
            reachy.l_arm.l_gripper: 0,
        }
        goto(
            goal_positions=left_scratch,
            duration=0.7,
            interpolation_mode=InterpolationMode.MINIMUM_JERK
        )


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
        goal_positions=left_base_position,
        duration=1.0,
        interpolation_mode=InterpolationMode.MINIMUM_JERK
    )
    
 
    reachy.head.look_at(0.5, 0, 0, duration=0.60)
    reachy.head.l_antenna.speed_limit = 20.0 
    reachy.head.r_antenna.speed_limit = 20.0 
    reachy.head.l_antenna.goal_position = 0.0
    reachy.head.r_antenna.goal_position = 0.0
    reachy.turn_off_smoothly("l_arm")
    reachy.turn_off("head")
     
    
