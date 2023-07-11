# robot-ludens

Robot Ludens is a research project that aims to program the robot Reachy from Pollen Robotics to play board games with humans.

## Original project Repositorys

- [GameStrategy](https://github.com/navesaurus/Reachy_tictactoe)
- [Movement](https://github.com/alpakadev/robot-ludens)
- Perception

## Requirements

- Unity-editor-Version: `2021.3.20f1`
- reachy-simulator-Version: `1.1`
- grpc-Unity-package: the most recent one will work

## How to execute Project

We still recommend reading the comments in the main file first. If all dependencys are installed, navigate into this Project folder.
Execute the `main.py` or the variations `main_real_reachy.py`, `main_simulation.py`

```shell
python3 Pythonscripts/main.py
```

## Installation Guide for the Unity Project

1. Download the Unity package available on the [release page](https://github.com/pollen-robotics/Simulator_Reachy2021/releases). Download the [grpc_unity_package](https://packages.grpc.io/archive/2022/04/67538122780f8a081c774b66884289335c290cbe-f15a2c1c-582b-4c51-acf2-ab6d711d2c59/csharp/grpc_unity_package.2.47.0-dev202204190851.zip) from the gRPC daily builds.
2. In your Unity Project import the unity package via Assets (From the menu Assets/Import Package/Custom Package…, import reachy2021-simulator.unitypackage)
3. Add grpc_unity_package (plugins) via drag and drop in the Assets folder of the project window.

The Assets folder should look like this:

```shell
Assets
|
+--- ...
|
+--- Plugins  (grpc module)
|
+--- ReachySimulator 
|
+--- ...
```

### Reachy-SDK Dependency

ReachySDK for the connection to the robot.

#### Real Reachy

Terminal:

```console
python3 -m pip install reachy-sdk=0.7.0
```

#### Simulation requiremnts

To enable head movements via look_at or (reachy.head.neck_roll, reachy.head.neck_pitch, reachy.head.neck_yaw) reachy-sdk version 0.4.0 and reachy_sdk_api version 0.4.5 have to be installed!

Terminal:

```console
python3 -m pip install reachy-sdk==0.4.0 
python3 -m pip install reachy-sdk-api==0.4.5
```

To install to newest version enter:

```python
python3 -m pip install reachy-sdk
```

### Other Dependencies

The following modules are also needed:

```python
pip install pyyaml
pip install face_recognition
pip install dlib
pip install playsound
```

