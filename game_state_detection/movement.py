def goal_position(reachy):
    try:
        reachy.head.look_at(0.5, 0, -0.6, duration=1)
    except TypeError:
        reachy.head.look_at(0.5, 0, -0.6, 1, "simul")

def base_position(reachy):
    try:
        reachy.head.look_at(0.5, 0, 0, duration=1)
    except TypeError:
        reachy.head.look_at(0.5, 0, 0, 1, "simul")