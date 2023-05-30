# TODO: Move this to Movement Module
from Movement.MoveFacade import MoveFacade 

def goal_position(reachy,move: MoveFacade):
    try:
        #reachy.head.look_at(0.5, 0, -0.6, duration=1)
        move.do_move_head([0.5, 0, -0.6])
    except TypeError:
        print("type error")
        reachy.head.look_at(0.5, 0, -0.6, 1, "simul")

def base_position(reachy,move: MoveFacade):
    try:
        #reachy.head.look_at(0.5, 0, 0, duration=1)
        move.do_move_head([0.5, 0, -0.6])
    except TypeError:
        print("type error")
        reachy.head.look_at(0.5, 0, 0, 1, "simul")