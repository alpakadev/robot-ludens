from reachy_sdk import ReachySDK
from reachy_sdk.trajectory import goto
from reachy_sdk.trajectory.interpolation import InterpolationMode
import numpy as np
import time

reachy = ReachySDK(host='localhost')

for name, joint in reachy.joints.items(): 
    print(f'Joint "{name}" is at pos {joint.present_position} degree.') 

x = 0.0
y = 0.0
z = 0.0

openhand = {
    reachy.r_arm.r_gripper : -60,
    }

closedhand = {
    reachy.r_arm.r_gripper : 10,
    }



def on():
    reachy.turn_on('r_arm')
    reachy.turn_on('l_arm')
    
def off():
    reachy.turn_off_smoothly('r_arm')
    


def move(x,y,z):
    A = np.array([
      [0, 0, -1, x],
      [0, 1, 0, y],  
      [1, 0, 0, z],
      [0, 0, 0, 1],  
    ])
    joint_pos_A = reachy.r_arm.inverse_kinematics(A)
    goto({joint: pos for joint,pos in zip(reachy.r_arm.joints.values(), joint_pos_A)}, duration=1.0)
    time.sleep(0.5)
    
    
def moveleft(x,y,z):
    A = np.array([
      [0, 0, -1, x],
      [0, 1, 0, y],  
      [1, 0, 0, z],
      [0, 0, 0, 1],  
    ])
    joint_pos_A = reachy.l_arm.inverse_kinematics(A)
    goto({joint: pos for joint,pos in zip(reachy.l_arm.joints.values(), joint_pos_A)}, duration=1.0)
    time.sleep(0.5)
    
    
def firstmoving():
    move(0.4,-0.2,-0.2)
    moveleft(0.4,0.2,-0.2)
    move(0.2,-0.27,-0.3)
    goto(goal_positions=openhand,duration= 1.0)
    move(0.4,-0.27,-0.3)
    move(0.4,-0.27,-0.38)
    move(0.41,-0.29,-0.39)
    goto(goal_positions=closedhand,duration= 1.0)
    move(0.4,-0.27,-0.2)
    move(0.32,-0.18,-0.2)
    move(0.32,-0.18,-0.37)
    goto(goal_positions=openhand,duration= 1.0)
    move(0.32,-0.18,-0.2)
    move(0.2,-0.27,-0.3)