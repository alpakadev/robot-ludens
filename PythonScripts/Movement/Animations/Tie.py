import time
from reachy_sdk.trajectory import goto
from reachy_sdk.trajectory.interpolation import InterpolationMode
def animation_tie(reachy): 
    """
    reaction to tie, shoulder shrugging 
    """
    reachy.turn_on("head")
    reachy.turn_on("l_arm")
    reachy.turn_on("r_arm")
    reachy.head.l_antenna.speed_limit = 90.0
    reachy.head.r_antenna.speed_limit = 90.0

    tie_start = {
        reachy.r_arm.r_shoulder_pitch: 5,
        reachy.r_arm.r_shoulder_roll: -10,  # moves left to right
        reachy.r_arm.r_arm_yaw: -60,  # forward/back
        reachy.r_arm.r_elbow_pitch: -120,
        reachy.r_arm.r_forearm_yaw: -70,
        reachy.r_arm.r_wrist_pitch: 5,
        reachy.r_arm.r_wrist_roll: 0,
        reachy.r_arm.r_gripper: 40,

        reachy.l_arm.l_shoulder_pitch: 5,
        reachy.l_arm.l_shoulder_roll: 10,  # moves left to right
        reachy.l_arm.l_arm_yaw: 60,  # forward/back
        reachy.l_arm.l_elbow_pitch: -120, #mit oder ohne minus?
        reachy.l_arm.l_forearm_yaw: 70,
        reachy.l_arm.l_wrist_pitch: 5,
        reachy.l_arm.l_wrist_roll: 0,
        reachy.l_arm.l_gripper: -40,

        reachy.head.l_antenna: -45,
        reachy.head.r_antenna: 45,  
        reachy.head.neck_roll: -10,  # tilt +left to -right 35
        reachy.head.neck_pitch: 20,   # up down
        reachy.head.neck_yaw: -15,
    }

    goto(
        goal_positions=tie_start,
        duration=1.0,
        interpolation_mode=InterpolationMode.MINIMUM_JERK,
        )
   
    #shrugging 
    for _ in range(2):

        tie_up = {
            reachy.head.l_antenna: -35,
            reachy.head.r_antenna: 55,  
            reachy.head.neck_roll: -45,  
            reachy.head.neck_pitch: 10,  
            reachy.head.neck_yaw: 0,     
            reachy.r_arm.r_shoulder_pitch: 5,
            reachy.r_arm.r_shoulder_roll: -45,  
            reachy.r_arm.r_arm_yaw: -90,  
            reachy.r_arm.r_elbow_pitch: -110,
            reachy.r_arm.r_forearm_yaw: -20,
            reachy.r_arm.r_wrist_pitch: 45,
            reachy.r_arm.r_wrist_roll: 0,
            reachy.r_arm.r_gripper: 40,

            reachy.l_arm.l_shoulder_pitch: 5,
            reachy.l_arm.l_shoulder_roll: 45,  
            reachy.l_arm.l_arm_yaw: 90,  
            reachy.l_arm.l_elbow_pitch: -110,
            reachy.l_arm.l_forearm_yaw: 20,
            reachy.l_arm.l_wrist_pitch: 45,
            reachy.l_arm.l_wrist_roll: 0,
            reachy.l_arm.l_gripper: -40,

        }

        goto(
            goal_positions=tie_up,
            duration=1.0,
            interpolation_mode=InterpolationMode.MINIMUM_JERK,
        )
    
        goto(
            goal_positions=tie_start,
            duration=1.0,
            interpolation_mode=InterpolationMode.MINIMUM_JERK,
        )
            
        
    reachy.head.look_at(0.5, 0, 0, duration = 0.8)
    reachy.head.l_antenna.goal_position = -55.0
    reachy.head.r_antenna.goal_position = 35.0
    time.sleep(1)
  
    #go back to default
    arms_base_position = {
        reachy.r_arm.r_shoulder_pitch: -25,
        reachy.r_arm.r_shoulder_roll: -20,  # moves left to right
        reachy.r_arm.r_arm_yaw: 15,  # forward/back
        reachy.r_arm.r_elbow_pitch: -40,
        reachy.r_arm.r_forearm_yaw: -15,
        reachy.r_arm.r_wrist_pitch: -25,
        reachy.r_arm.r_wrist_roll: 0,
        reachy.r_arm.r_gripper: 0,
    
        reachy.l_arm.l_shoulder_pitch: -25,
        reachy.l_arm.l_shoulder_roll: 0,  # moves left to right
        reachy.l_arm.l_arm_yaw: 15,  # forward/back
        reachy.l_arm.l_elbow_pitch: -40,
        reachy.l_arm.l_forearm_yaw: -20,
        reachy.l_arm.l_wrist_pitch: -25,
        reachy.l_arm.l_wrist_roll: 0,
        reachy.l_arm.l_gripper: 0,
    }

    goto(
        goal_positions=arms_base_position,
        duration=1.20,
        interpolation_mode=InterpolationMode.MINIMUM_JERK
    )
 
    reachy.head.look_at(0.5, 0, 0, 1)
    reachy.head.r_antenna.goal_position = 0.0
    reachy.head.l_antenna.goal_position = 0.0
    time.sleep(1)

    reachy.turn_off_smoothly("l_arm")
    reachy.turn_off_smoothly("r_arm")
    reachy.turn_off_smoothly("head")



   





    