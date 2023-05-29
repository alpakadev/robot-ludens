import time
from reachy_sdk.trajectory import goto
from reachy_sdk.trajectory.interpolation import InterpolationMode
from Happy import animation_happy


def animation_win(reachy):
    reachy.turn_on("l_arm")
    reachy.head.look_at(0.5, 0, -0.4, duration=1.0)
    time.sleep(0.5)
    reachy.head.l_antenna.goal_position = 50.0
    reachy.head.r_antenna.goal_position = -50.0
    reachy.head.look_at(0.05, 0, 0, duration=0.5)
    time.sleep(1.0)

    animation_happy(reachy)

    for i in range(3):
        right_up_position = {
            reachy.r_arm.r_shoulder_pitch: -60,
            reachy.r_arm.r_shoulder_roll: -10,
            reachy.r_arm.r_arm_yaw: 25,
            reachy.r_arm.r_elbow_pitch: -125,
            reachy.r_arm.r_forearm_yaw: 15,
            reachy.r_arm.r_wrist_pitch: 25,
            reachy.r_arm.r_wrist_roll: 20,
            reachy.r_arm.r_gripper: 40,
        }
        left_up_position = {
            reachy.l_arm.l_shoulder_pitch: -60,
            reachy.l_arm.l_shoulder_roll: -10,
            reachy.l_arm.l_arm_yaw: 25,
            reachy.l_arm.l_elbow_pitch: -125,
            reachy.l_arm.l_forearm_yaw: 15,
            reachy.l_arm.l_wrist_pitch: 25,
            reachy.l_arm.l_wrist_roll: 20,
            reachy.l_arm.l_gripper: 40,
        }

        animation_happy(reachy)

        goto(
            goal_positions=left_up_position,
            duration=0.30,
            interpolation_mode=InterpolationMode.MINIMUM_JERK
        )
        goto(
            goal_positions=right_up_position,
            duration=0.30,
            interpolation_mode=InterpolationMode.MINIMUM_JERK
        )

        right_up2_position = {
            reachy.r_arm.r_shoulder_pitch: -50,
            reachy.r_arm.r_shoulder_roll: -15,
            reachy.r_arm.r_arm_yaw: -10,
            reachy.r_arm.r_elbow_pitch: -120,
            reachy.r_arm.r_forearm_yaw: -15,
            reachy.r_arm.r_wrist_pitch: -5,
            reachy.r_arm.r_wrist_roll: -20,
            reachy.r_arm.r_gripper: -30,
        }
        left_up2_position = {
            reachy.l_arm.l_shoulder_pitch: -50,
            reachy.l_arm.l_shoulder_roll: -15,
            reachy.l_arm.l_arm_yaw: -10,
            reachy.l_arm.l_elbow_pitch: -120,
            reachy.l_arm.l_forearm_yaw: -15,
            reachy.l_arm.l_wrist_pitch: -5,
            reachy.l_arm.l_wrist_roll: -20,
            reachy.l_arm.l_gripper: -30,
        }
        animation_happy(reachy)
        goto(
            goal_positions=left_up2_position,
            duration=0.30,
            interpolation_mode=InterpolationMode.MINIMUM_JERK
        )
        goto(
            goal_positions=right_up2_position,
            duration=0.30,
            interpolation_mode=InterpolationMode.MINIMUM_JERK
        )
    reachy.turn_off_smoothly("l_arm")
