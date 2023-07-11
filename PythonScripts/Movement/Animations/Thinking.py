import time
import random

from ..constants import THINKING
from .Player import play_sound
from ..Helper.Safely import safely_run
from reachy_sdk.trajectory import goto
from reachy_sdk.trajectory.interpolation import InterpolationMode


def animation_thinking(reachy, use_sound):
    """
    Scratch head with hand
    """
    reachy.turn_on("head")
    reachy.turn_on("l_arm")

    reachy.head.look_at(0.5, -0.3, -0.2, duration=1.0)
    reachy.head.l_antenna.goal_position = 40.0
    reachy.head.r_antenna.goal_position = -80.0
    time.sleep(0.50)

    for x in range(3):
        degree = random.randint(20, 55)

        left_touch_head_position = {
            reachy.l_arm.l_shoulder_pitch: -80,
            reachy.l_arm.l_shoulder_roll: 20,
            reachy.l_arm.l_arm_yaw: -27,
            reachy.l_arm.l_elbow_pitch: -125,
            reachy.l_arm.l_forearm_yaw: -10,
            reachy.l_arm.l_wrist_pitch: -45,
            reachy.l_arm.l_wrist_roll: 0,
            reachy.l_arm.l_gripper: 0,
        }

        goto(
            goal_positions=left_touch_head_position,
            duration=1.5,
            interpolation_mode=InterpolationMode.MINIMUM_JERK
        )
        time.sleep(0.1)

        if x == 0:
            safely_run(play_sound(random.choice(THINKING), False),
                       "[Anim Thinking] Sound konnte nicht abgespielt werden") if use_sound else None

        reachy.head.l_antenna.speed_limit = 90.0 - degree // 2
        reachy.head.r_antenna.speed_limit = 60.0 - degree // 2
        reachy.head.l_antenna.goal_position = 50.0 - degree
        reachy.head.r_antenna.goal_position = -90.0 + degree
        time.sleep(0.1)

        left_scratch = {
            reachy.l_arm.l_shoulder_pitch: -75,
            reachy.l_arm.l_shoulder_roll: 20,
            reachy.l_arm.l_arm_yaw: -27,
            reachy.l_arm.l_elbow_pitch: -125,
            reachy.l_arm.l_forearm_yaw: -10,
            reachy.l_arm.l_wrist_pitch: 0,
            reachy.l_arm.l_wrist_roll: 0,
            reachy.l_arm.l_gripper: 0,
        }

        goto(
            goal_positions=left_scratch,
            duration=0.80,
            interpolation_mode=InterpolationMode.MINIMUM_JERK
        )

    # back to default
    left_base_position = {
        reachy.l_arm.l_shoulder_pitch: -25,
        reachy.l_arm.l_shoulder_roll: 0,
        reachy.l_arm.l_arm_yaw: 15,
        reachy.l_arm.l_elbow_pitch: -40,
        reachy.l_arm.l_forearm_yaw: -20,
        reachy.l_arm.l_wrist_pitch: -25,
        reachy.l_arm.l_wrist_roll: 0,
        reachy.l_arm.l_gripper: 20,
    }

    goto(
        goal_positions=left_base_position,
        duration=1.2,
        interpolation_mode=InterpolationMode.MINIMUM_JERK
    )

    reachy.head.look_at(0.5, 0, 0, duration=0.60)
    reachy.head.l_antenna.speed_limit = 20.0
    reachy.head.r_antenna.speed_limit = 20.0
    reachy.head.l_antenna.goal_position = 0.0
    reachy.head.r_antenna.goal_position = 0.0

    reachy.turn_off_smoothly("l_arm")
    time.sleep(1.0)
    reachy.turn_off_smoothly("head")
