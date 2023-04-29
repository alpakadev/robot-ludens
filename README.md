# robot-ludens
Robot Ludens is a research project that aims to program the robot Reachy from Pollen Robotics to play board games with humans.

## Original project Repositorys:
- [GameStrategy](https://github.com/navesaurus/Reachy_tictactoe)
- [Movement](https://github.com/alpakadev/robot-ludens)
- Perception

## Installation Guide

1. Download the Unity package available on the [release page](https://github.com/pollen-robotics/Simulator_Reachy2021/releases). Download the [grpc_unity_package](https://packages.grpc.io/archive/2022/04/67538122780f8a081c774b66884289335c290cbe-f15a2c1c-582b-4c51-acf2-ab6d711d2c59/csharp/grpc_unity_package.2.47.0-dev202204190851.zip) from the gRPC daily builds.
2. In your Unity Project import the unity package via Assets (From the menu Assets/Import Package/Custom Package…, import reachy2021-simulator.unitypackage)
3. Add grpc_unity_package (plugins) via drag and drop in the Assets folder of the project window.

## Requirements 
- Unity-editor-Version: `2021.3.20f1`
- reachy-simulator-Version: `1.1` (Has to be changed for head Movement etc.!)
- grpc-Unity-package: the most recent one will work

### Reachy-SDK
ReachySDK for the connection to the robot, goto to generate trajectories, and InterpolationMode to choose the pattern of these trajectories. Time to monitor the temporality of our movements. Numpty creates coordinate systems for inverse kinematics. 

Terminal:
```concol
  python3 -m pip install reachy-sdk
```
  
To enable head movements via look_at or (reachy.head.neck_roll, reachy.head.neck_pitch, reachy.head.neck_yaw) reachy-sdk version 0.40 and reachy_sdk_api version 0.4.5 have to be installed!
  
Terminal:
```consol
  python3 -m pip uninstall reachy-sdk-api 
  
  python3 -m pip uninstall reachy-sdk 
  
  python3 -m pip install reachy-sdk==0.4.0 
  
  python3 -m pip install reachy-sdk-api==0.4.5
  
  ```

to switch to newest version enter: 
```
  python3 -m pip install reachy-sdk
```

Usage in Python:

```python
  
  from reachy_sdk import ReachySDK 
  
  from reachy_sdk.trajectory import goto 
  
  from reachy_sdk.trajectory.interpolation import InterpolationMode 
  
  import numpy as np
  
  import time
```



## Python Script Guide
TODO: Information about which python file to execute to Play the Game; A Guide which functions to call from each group.
