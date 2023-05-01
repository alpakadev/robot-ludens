'''
This is the test script that needs to be executed 
in order to test Reachys ability to detect colors.

After starting the script, you can stop it by pressing q.
'''

from reachy_sdk import ReachySDK
import time
from detection import get_board_cases

def reachy_test_module():
    reachy = ReachySDK(host='localhost')
    reachy.head.compliant = False
    time.sleep(0.1)

    # move head to goal position
    goal_position = reachy.head.look_at(0.5, 0, -0.40, duration=1)

    board_cases = get_board_cases(reachy)

    # print board_cases
    for line in board_cases:
        print ('  '.join(map(str, line)))

    # moving reachys arms and move game pieces
    # ...........

    # move head back to base position
    reachy.head.look_at(0.5, 0, 0, duration=1)
    time.sleep(0.2)
    reachy.head.compliant = True


reachy_test_module()