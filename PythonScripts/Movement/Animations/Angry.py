import time

from reachy_sdk.trajectory import goto
from reachy_sdk.trajectory.interpolation import InterpolationMode


def animation_angry(reachy):
    """
    pushes cylinders and cubes of the board
    """
    reachy.turn_on("head")
    reachy.turn_on("r_arm")

    reachy.head.l_antenna.speed_limit = 50.0
    reachy.head.r_antenna.speed_limit = 50.0 

    reachy.head.look_at(0.5, -0.4, -0.4, duration=1.0) 
    time.sleep(1.0)
    reachy.head.l_antenna.goal_position = -90
    reachy.head.r_antenna.goal_position = 90

    time.sleep(0.1)
    
    reachy.head.l_antenna.goal_position = -110
    reachy.head.r_antenna.goal_position = 110

    time.sleep(0.8)

    r_start_position = {
        reachy.r_arm.r_shoulder_pitch: -20,
        reachy.r_arm.r_shoulder_roll: -60,   # moves left to right
        reachy.r_arm.r_arm_yaw: 30,    # forward/back
        reachy.r_arm.r_elbow_pitch: -70,
        reachy.r_arm.r_forearm_yaw: -40,
        reachy.r_arm.r_wrist_pitch: -20,
        reachy.r_arm.r_wrist_roll: 0,
        reachy.r_arm.r_gripper: 0,
        }
    goto(
        goal_positions=r_start_position,
        duration = 2.3,
        interpolation_mode=InterpolationMode.MINIMUM_JERK
        )
    r_sweep_position = {
        reachy.r_arm.r_shoulder_pitch: -25, #up / down if too high try -25/-20
        reachy.r_arm.r_shoulder_roll: 20,  # moves left to right
        reachy.r_arm.r_arm_yaw: 10,
        reachy.r_arm.r_elbow_pitch: -40,
        reachy.r_arm.r_forearm_yaw: 0,
        reachy.r_arm.r_wrist_pitch: -20,
        reachy.r_arm.r_wrist_roll: 0,
        reachy.r_arm.r_gripper: 0,
        }
    goto(
        goal_positions=r_sweep_position,
        duration = 2.3,
        interpolation_mode=InterpolationMode.MINIMUM_JERK
        )

    rbase_position = {
        reachy.r_arm.r_shoulder_pitch: -23,
        reachy.r_arm.r_shoulder_roll: -45,    # moves left to right
        reachy.r_arm.r_arm_yaw: 30,    # forward/back
        reachy.r_arm.r_elbow_pitch: -70,
        reachy.r_arm.r_forearm_yaw: 0,
        reachy.r_arm.r_wrist_pitch: -20,
        reachy.r_arm.r_wrist_roll: 0,
        reachy.r_arm.r_gripper: 0,
        }
    goto(
        goal_positions=rbase_position,
        duration=2.3,
        interpolation_mode=InterpolationMode.MINIMUM_JERK
        )
   
    time.sleep(1.0)
    reachy.head.l_antenna.goal_position = -30
    reachy.head.r_antenna.goal_position = 30
    reachy.head.look_at(0.5, 0, 0, duration=1.0)
    time.sleep(1.0)
    reachy.head.l_antenna.goal_position = -110
    reachy.head.r_antenna.goal_position = 110
    time.sleep(2.0)

   # for _ in range(4):
      # reachy.head.l_antenna.speed_limit = 20.0 
       # reachy.head.r_antenna.speed_limit = 20.0
       # reachy.head.l_antenna.goal_position = -10
       # reachy.head.r_antenna.goal_position = 10

       # time.sleep(0.5)
    
        #reachy.head.l_antenna.goal_position = 20
        #reachy.head.r_antenna.goal_position = -20

    
    time.sleep(0.1)
    reachy.turn_off_smoothly("r_arm")
    time.sleep(0.1)
    reachy.head.l_antenna.goal_position = 0.0
    time.sleep(0.1)
    reachy.head.r_antenna.goal_position = 0.0
   

    

