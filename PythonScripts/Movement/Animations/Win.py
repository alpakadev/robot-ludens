import time
import random

from ..constants import WINNING
from .Player import play_sound
from ..Helper.Safely import safely_run
from reachy_sdk.trajectory import goto
from reachy_sdk.trajectory.interpolation import InterpolationMode


# from .HappyAntennas import animation_happy_antennas


def animation_win(reachy, use_sound):
    """
    arms up and down with grippers opening/closing as head moves
    """
    reachy.turn_on("head")
    reachy.turn_on("r_arm")
    reachy.turn_on("l_arm")

    reachy.head.look_at(0.05, 0, -0.05, duration=1.0)
    time.sleep(0.5)

    safely_run(play_sound(random.choice(WINNING), False),
               "[Anim Win] Sound konnte nicht abgespielt werden") if use_sound else None

    reachy.head.look_at(0.5, 0, 0, duration=0.5)
    time.sleep(0.2)

    for _ in range(4):
        arms_up_position = {
            reachy.head.l_antenna: 30,
            reachy.head.r_antenna: -30,
            reachy.head.neck_roll: -15,
            reachy.head.neck_pitch: 2,
            reachy.head.neck_yaw: -3,

            reachy.r_arm.r_shoulder_pitch: -60,
            reachy.r_arm.r_shoulder_roll: 0,
            reachy.r_arm.r_arm_yaw: 0,
            reachy.r_arm.r_elbow_pitch: -120,
            reachy.r_arm.r_forearm_yaw: 0,
            reachy.r_arm.r_wrist_pitch: 0,
            reachy.r_arm.r_wrist_roll: 0,
            reachy.r_arm.r_gripper: 40,

            reachy.l_arm.l_shoulder_pitch: -60,
            reachy.l_arm.l_shoulder_roll: 0,
            reachy.l_arm.l_arm_yaw: 0,
            reachy.l_arm.l_elbow_pitch: -120,
            reachy.l_arm.l_forearm_yaw: 0,
            reachy.l_arm.l_wrist_pitch: 0,
            reachy.l_arm.l_wrist_roll: 0,
            reachy.l_arm.l_gripper: 40,

            reachy.head.l_antenna: -30,
            reachy.head.r_antenna: 30,
            reachy.head.neck_roll: 15,
            reachy.head.neck_pitch: -3,
            reachy.head.neck_yaw: 2,
        }

        goto(
            goal_positions=arms_up_position,
            duration=0.75,
            interpolation_mode=InterpolationMode.MINIMUM_JERK
        )

        # animation_happy_antennas(reachy)

        arms_up2_position = {
            reachy.head.l_antenna: 40,
            reachy.head.r_antenna: -40,
            reachy.head.neck_roll: 10,
            reachy.head.neck_pitch: -2,
            reachy.head.neck_yaw: 3,
            reachy.r_arm.r_shoulder_pitch: -80,
            reachy.r_arm.r_shoulder_roll: 0,
            reachy.r_arm.r_arm_yaw: 0,
            reachy.r_arm.r_elbow_pitch: -120,
            reachy.r_arm.r_forearm_yaw: 0,
            reachy.r_arm.r_wrist_pitch: 0,
            reachy.r_arm.r_wrist_roll: 0,
            reachy.r_arm.r_gripper: -40,

            reachy.l_arm.l_shoulder_pitch: -80,
            reachy.l_arm.l_shoulder_roll: 0,
            reachy.l_arm.l_arm_yaw: 0,
            reachy.l_arm.l_elbow_pitch: -120,
            reachy.l_arm.l_forearm_yaw: 0,
            reachy.l_arm.l_wrist_pitch: 0,
            reachy.l_arm.l_wrist_roll: 0,
            reachy.l_arm.l_gripper: -40,

            reachy.head.l_antenna: 60,
            reachy.head.r_antenna: -60,
            reachy.head.neck_roll: -5,
            reachy.head.neck_pitch: 3,
            reachy.head.neck_yaw: -2,
        }

        goto(
            goal_positions=arms_up2_position,
            duration=0.75,
            interpolation_mode=InterpolationMode.MINIMUM_JERK
        )

    # go back to default
    arms_base_position = {
        reachy.r_arm.r_shoulder_pitch: -25,
        reachy.r_arm.r_shoulder_roll: -20,  # moves left to right
        reachy.r_arm.r_arm_yaw: 15,  # forward/back
        reachy.r_arm.r_elbow_pitch: -40,
        reachy.r_arm.r_forearm_yaw: -15,
        reachy.r_arm.r_wrist_pitch: -25,
        reachy.r_arm.r_wrist_roll: 0,
        reachy.r_arm.r_gripper: 20,

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
        goal_positions=arms_base_position,
        duration=1.0,
        interpolation_mode=InterpolationMode.MINIMUM_JERK
    )

    reachy.head.look_at(0.5, -0, 0, duration=0.5)
    reachy.head.l_antenna.goal_position = 0.0
    reachy.head.r_antenna.goal_position = 0.0
    time.sleep(1)

    reachy.turn_off_smoothly("l_arm")
    reachy.turn_off_smoothly("r_arm")
    reachy.turn_off_smoothly("head")
