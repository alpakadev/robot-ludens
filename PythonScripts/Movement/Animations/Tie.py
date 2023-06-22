import time
from reachy_sdk.trajectory import goto
from reachy_sdk.trajectory.interpolation import InterpolationMode
def animation_tie(reachy): 
    reachy.turn_on("head")
    reachy.turn_on("l_arm")
    reachy.turn_on("r_arm")

   
    tie_r_joint_values = [5, -20, -90, -130, 0, 5, 0, 15] #list with values for joints,
    #values in the same order as joints
    goto_r_pre_tie = {joint: value_joint for (joint, value_joint) in zip(list(reachy.r_arm.joints.values()), tie_r_joint_values)}
    goto(
        goal_positions=goto_r_pre_tie,
        duration=1.0,
        interpolation_mode=InterpolationMode.MINIMUM_JERK,
        )
    
    print(reachy.r_arm.joints, reachy.l_arm.joints, reachy.head)

    tie_l_joint_values = [5, 20, 90, -130, 0, 5, 0, -15] #list with values for joints,
    #values in the same order as joints
    goto_l_pre_tie = {joint: value_joint for (joint, value_joint) in zip(list(reachy.l_arm.joints.values()), tie_l_joint_values)}
    goto(
        goal_positions=goto_l_pre_tie,
        duration=1.0,
        interpolation_mode=InterpolationMode.MINIMUM_JERK,
        )
    

    #shoulder movement 
    for _ in range(2):
        reachy.head.l_antenna.speed_limit = 90.0
        reachy.head.r_antenna.speed_limit = 90.0

        reachy.head.l_antenna.goal_position = -35.0
        reachy.head.r_antenna.goal_position = 55.0

        head = {
        reachy.head.l_antenna: -35,
        reachy.head.r_antenna: 55,  
        reachy.head.neck_roll: 35,  # tilt +left to -right 35
        reachy.head.neck_pitch: 0,   # up down
        reachy.head.neck_yaw: 0,     # left to right side
        }
        goto(
            goal_positions=head,
            duration=1.0,
            interpolation_mode=InterpolationMode.MINIMUM_JERK
        )
    
        tie2_r_joint_values = [5, -45, -100, -130, -20, 45, 0, 15] #list with values for joints,
        #values in the same order as joints
        goto_r_pre_tie2 = {joint: value_joint for (joint, value_joint) in zip(list(reachy.r_arm.joints.values()), tie2_r_joint_values)}
        goto(
            goal_positions=goto_r_pre_tie2,
            duration=1.0,
            interpolation_mode=InterpolationMode.MINIMUM_JERK,
            )
    

        tie2_l_joint_values = [5, 45, 100, -130, 20, 45, 0, -15] #list with values for joints,
        #values in the same order as joints
        goto_l_pre_tie2 = {joint: value_joint for (joint, value_joint) in zip(list(reachy.l_arm.joints.values()), tie2_l_joint_values)}
        goto(
            goal_positions=goto_l_pre_tie2,
            duration=1.0,
            interpolation_mode=InterpolationMode.MINIMUM_JERK,
            )
        
        reachy.head.look_at(0.5, 0, 0, duration = 0.8)
        reachy.head.l_antenna.goal_position = -55.0
        reachy.head.r_antenna.goal_position = 35.0

        goto(
        goal_positions=goto_r_pre_tie,
        duration=1.0,
        interpolation_mode=InterpolationMode.MINIMUM_JERK,
        )

        goto(
        goal_positions=goto_l_pre_tie,
        duration=1.0,
        interpolation_mode=InterpolationMode.MINIMUM_JERK,
        )
        
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
        duration=1.20,
        interpolation_mode=InterpolationMode.MINIMUM_JERK
    )
    goto(
        goal_positions=left_base_position,
        duration=1.20,
        interpolation_mode=InterpolationMode.MINIMUM_JERK
    )
    
   
    reachy.head.look_at(0.5, 0, 0, 1)
    reachy.head.r_antenna.goal_position = 0.0
    reachy.head.l_antenna.goal_position = 0.0
    reachy.turn_off_smoothly("l_arm")
    reachy.turn_off_smoothly("r_arm")
    
    reachy.turn_off("head")



   





    