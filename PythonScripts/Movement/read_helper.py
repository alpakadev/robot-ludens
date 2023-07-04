from reachy_sdk import ReachySDK

reachy = ReachySDK(host="localhost")

while True:
    matrix = reachy.l_arm.forward_kinematics()
    x = round(matrix[0][3], 2)
    y = round(matrix[1][3], 2)
    z = -0.37
    res = [x, y, z]
    print(res)
    input()