import time

from reachy_sdk.trajectory import goto
from reachy_sdk.trajectory.interpolation import InterpolationMode


def animation_thinking(reachy):
    # Scratch head with hand
    
    reachy.head.look_at(0.5, -0.2, -0.1, duration=1.0)
    time.sleep(0.50)
    reachy.turn_on("l_arm")

    for _ in range(2):
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

        time.sleep(0.60)
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
            duration=1.0,
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
    
    reachy.turn_off_smoothly("l_arm") 
    reachy.head.look_at(0.5, 0, 0, duration=1.0)
