'''
This is the test script that needs to be executed 
in order to test Reachys ability to detect colors.

After starting the script, you can stop it by pressing q.
'''

from reachy_sdk import ReachySDK
import time
from movement import goal_position, base_position
from detection import get_board_cases

def main():
    # initialize Reachy
    reachy = ReachySDK(host='localhost')
    reachy.head.compliant = False
    time.sleep(0.1)

    # move head to goal position
    goal_position(reachy)

    board_cases = get_board_cases(reachy)

    # print board_cases
    for line in board_cases:
        print ('  '.join(map(str, line)))

    # moving reachys arms and move game pieces
    # ...........

    # move head to base position
    base_position(reachy)
    time.sleep(0.2)
    reachy.head.compliant = True


if __name__ == '__main__':
    main()