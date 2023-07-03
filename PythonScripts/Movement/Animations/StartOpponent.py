import time
from reachy_sdk.trajectory import goto
from reachy_sdk.trajectory.interpolation import InterpolationMode

def animation_start_opponent(reachy):
    
    reachy.turn_on("l_arm")
    reachy.turn_on("head")
    reachy.head.l_antenna.speed_limit = 40.0
    reachy.head.r_antenna.speed_limit = 40.0

    reachy.head.l_antenna.goal_position = 30.0
    reachy.head.r_antenna.goal_position = -40.0

    
    l_arm_start = {
        reachy.l_arm.l_shoulder_pitch: -25, #up or down
        reachy.l_arm.l_shoulder_roll: 10,   # moves left to right
        reachy.l_arm.l_arm_yaw: -25,    # forward/back
        reachy.l_arm.l_elbow_pitch: -105,
        reachy.l_arm.l_forearm_yaw: 0,
        reachy.l_arm.l_wrist_pitch: 0,
        reachy.l_arm.l_wrist_roll: 0,
        reachy.l_arm.l_gripper: -40,
        }
    
    goto(
        goal_positions=l_arm_start,
        duration = 1.0,
        interpolation_mode=InterpolationMode.MINIMUM_JERK
        )
    l_arm = {
        reachy.l_arm.l_shoulder_pitch: -25, #up or down
        reachy.l_arm.l_shoulder_roll: -5,   # moves left to right
        reachy.l_arm.l_arm_yaw: -20,    # forward/back
        reachy.l_arm.l_elbow_pitch: -90,
        reachy.l_arm.l_forearm_yaw: 0,
        reachy.l_arm.l_wrist_pitch: 0,
        reachy.l_arm.l_wrist_roll: 0,
        reachy.l_arm.l_gripper: -40,
        }
    
    head = {
            reachy.head.l_antenna: 45,
            reachy.head.r_antenna: 20,  
            reachy.head.neck_roll: -15,  # tilt +left to -right 35
            reachy.head.neck_pitch: 5,   # up down
            reachy.head.neck_yaw: 5,     # left to right side
            }
    
    goto(
        goal_positions=head,
        duration=1.0,
        interpolation_mode=InterpolationMode.MINIMUM_JERK
        )
    
    goto(
        goal_positions=l_arm,
        duration = 1.0,
        interpolation_mode=InterpolationMode.MINIMUM_JERK
        )
    
    for _ in range(2):

        goto(
        goal_positions=l_arm_start,
        duration = 1.3,
        interpolation_mode=InterpolationMode.MINIMUM_JERK
        )
        reachy.head.l_antenna.goal_position = 50.0
        reachy.head.r_antenna.goal_position = -20.0

        goto(
        goal_positions=l_arm,
        duration = 1.3,
        interpolation_mode=InterpolationMode.MINIMUM_JERK
        )

        reachy.head.l_antenna.goal_position = 30.0
        reachy.head.r_antenna.goal_position = -40.0
        

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
    time.sleep(2.0)
    goto(
        goal_positions=left_base_position,
        duration=1.0,
        interpolation_mode=InterpolationMode.MINIMUM_JERK
    )
    reachy.head.l_antenna.goal_position = 0.0
    reachy.head.r_antenna.goal_position = 0.0
    reachy.head.look_at(0.5, 0, 0, 1)
    reachy.turn_off_smoothly("l_arm")
    