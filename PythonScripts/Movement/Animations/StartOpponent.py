import random
import time

from reachy_sdk.trajectory import goto
from reachy_sdk.trajectory.interpolation import InterpolationMode

from ..constants import START_HUMAN
from ..Helper.Safely import safely_run
from .Player import play_sound


def animation_start_opponent(reachy, use_sound):
    """
    pointing at opponent to start playing 
    """
    reachy.turn_on("l_arm")
    reachy.turn_on("head")
    reachy.head.l_antenna.speed_limit = 40.0
    reachy.head.r_antenna.speed_limit = 40.0

    reachy.head.l_antenna.goal_position = 30.0
    reachy.head.r_antenna.goal_position = -40.0

    l_arm_start = {
        reachy.head.l_antenna: 45,
        reachy.head.r_antenna: 20,
        reachy.head.neck_roll: -5,  # tilt +left to -right 35
        reachy.head.neck_pitch: 5,  # up down
        reachy.head.neck_yaw: 15,  # left to right side
        reachy.l_arm.l_shoulder_pitch: -20,
        reachy.l_arm.l_shoulder_roll: 10,  # moves left to right
        reachy.l_arm.l_arm_yaw: -20,  # forward/back
        reachy.l_arm.l_elbow_pitch: -90,
        reachy.l_arm.l_forearm_yaw: 0,
        reachy.l_arm.l_wrist_pitch: 0,
        reachy.l_arm.l_wrist_roll: 0,
        reachy.l_arm.l_gripper: -40,
    }

    goto(
        goal_positions=l_arm_start,
        duration=1.3,
        interpolation_mode=InterpolationMode.MINIMUM_JERK
    )

    head_tilt_r = {
        reachy.head.l_antenna: 45,
        reachy.head.r_antenna: 20,
        reachy.head.neck_roll: 5,  # tilt +left to -right 35
        reachy.head.neck_pitch: 5,  # up down
        reachy.head.neck_yaw: -5,
    }

    goto(
        goal_positions=head_tilt_r,
        duration=1.0,
        interpolation_mode=InterpolationMode.MINIMUM_JERK,
    )

    time.sleep(0.1)

    for x in range(2):

        l_arm_tilted_head = {
            reachy.head.l_antenna: 45,
            reachy.head.r_antenna: 20,
            reachy.head.neck_roll: 13,  # tilt +left to -right 35
            reachy.head.neck_pitch: 5,  # up down
            reachy.head.neck_yaw: -5,  # left to right side
            reachy.l_arm.l_shoulder_pitch: -25,
            reachy.l_arm.l_shoulder_roll: 10,  # moves left to right
            reachy.l_arm.l_arm_yaw: -35,  # forward/back
            reachy.l_arm.l_elbow_pitch: -105,
            reachy.l_arm.l_forearm_yaw: 0,
            reachy.l_arm.l_wrist_pitch: 0,
            reachy.l_arm.l_wrist_roll: 0,
            reachy.l_arm.l_gripper: -40,
        }

        goto(
            goal_positions=l_arm_tilted_head,
            duration=1.3,
            interpolation_mode=InterpolationMode.MINIMUM_JERK
        )

        if x == 0:
            safely_run(play_sound(random.choice(START_HUMAN), False),
                       "[Anim StartOpponent] Sound konnte nicht abgespielt werden") if use_sound else None

        l_arm_point_tilted_head = {
            reachy.head.l_antenna: 50,
            reachy.head.r_antenna: -10,
            reachy.head.neck_roll: -5,  # tilt +left to -right 35
            reachy.head.neck_pitch: 2,  # up down
            reachy.head.neck_yaw: 3,  # left to right side
            reachy.l_arm.l_shoulder_pitch: -30,
            reachy.l_arm.l_shoulder_roll: -5,  # moves left to right
            reachy.l_arm.l_arm_yaw: -10,  # forward/back
            reachy.l_arm.l_elbow_pitch: -70,
            reachy.l_arm.l_forearm_yaw: 0,
            reachy.l_arm.l_wrist_pitch: 0,
            reachy.l_arm.l_wrist_roll: 0,
            reachy.l_arm.l_gripper: -40,
        }

        goto(
            goal_positions=l_arm_point_tilted_head,
            duration=1.3,
            interpolation_mode=InterpolationMode.MINIMUM_JERK
        )

        reachy.head.l_antenna.goal_position = 30.0
        reachy.head.r_antenna.goal_position = -40.0

    time.sleep(2.0)
    l_arm_base = {
        reachy.l_arm.l_shoulder_pitch: -25,
        reachy.l_arm.l_shoulder_roll: 0,  # moves left to right
        reachy.l_arm.l_arm_yaw: 15,  # forward/back
        reachy.l_arm.l_elbow_pitch: -40,
        reachy.l_arm.l_forearm_yaw: -20,
        reachy.l_arm.l_wrist_pitch: -25,
        reachy.l_arm.l_wrist_roll: 0,
        reachy.l_arm.l_gripper: 20,
    }

    goto(
        goal_positions=l_arm_base,
        duration=1.0,
        interpolation_mode=InterpolationMode.MINIMUM_JERK
    )

    reachy.head.l_antenna.goal_position = 0.0
    reachy.head.r_antenna.goal_position = 0.0
    reachy.head.look_at(0.5, 0, 0, 1)
    reachy.turn_off_smoothly("l_arm")
    time.sleep(1)

    reachy.turn_off_smoothly("head")
