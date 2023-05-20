# robot-ludens

Robot Ludens is a research project that aims to program the robot Reachy from Pollen Robotics to play board games with humans.

## Original project Repositorys

- [GameStrategy](https://github.com/navesaurus/Reachy_tictactoe)
- [Movement](https://github.com/alpakadev/robot-ludens)
- Perception

## Organisation des Projekts

Jedes Team hat erstmal einen eigenen Branch zum sammeln und organisieren von Code. Wenn ein Team mit einem Modul oder Submodul fertig ist bzw. wenn wir uns auf eine Projekt Struktur geeinigt haben können die einzelnen Branches mit dem Main Branch gemerged werden.
Für die Versionierung eurer Branches könnt ihr gerne eigene Tags erstellen (z. B. bewegung-0.1.0 oder strategie-modulname), damit kein Durcheinander entsteht und einzelne Branches immer direkt zugeordnet werden können. Achtet also bitte darauf, nur in die von euch genutzten Branches zu pushen und keine anderen Branches zu beeinflussen.

Auf keinen Fall Dateien mit sensiblen Daten (z. B. Passwörter oder Keys) in das Repository hochladen.

## UnityInstallation Guide

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

```console
  python3 -m pip install reachy-sdk
```
  
To enable head movements via look_at or (reachy.head.neck_roll, reachy.head.neck_pitch, reachy.head.neck_yaw) reachy-sdk version 0.40 and reachy_sdk_api version 0.4.5 have to be installed!
  
Terminal:

```console
  python3 -m pip uninstall reachy-sdk-api 
  
  python3 -m pip uninstall reachy-sdk 
  
  python3 -m pip install reachy-sdk==0.4.0 
  
  python3 -m pip install reachy-sdk-api==0.4.5
  
  ```

to switch to newest version enter:

```python
  python3 -m pip install reachy-sdk
```

## Perception Guide

Downloadlink für die aktuelle Unity-Szene mit Reachy, TicTacToe Feld, und roten/grünen Spielfiguren:
    https://gigamove.rwth-aachen.de/en/download/813dc3dff83f48f2163327a79cddf5d7

### Look-At-Fix

Angepasste SDK um die look_at Funktion in der Simulation nutzen zu können.

Nutzung:
    - Für die Arbeit mit der Simulation:
        reachy.head.look_at(x, y, z, duration, "simul")
    - Für die Arbeit mit dem Roboter, falls o.g. nicht funktioniert:
        reachy.head.look_at(x, y, z, duration, "real")
        Das ist der Weg, der in der aktuellen SDK eingeschlagen wird, der zu einem Blocking Error führt

Installation:
    - Linux:
        In /usr/local/lib/python<Version>/site-packages:
            reachy_sdk-0.7.0-py<Version>.zip aus dem git in reachy_sdk-0.7.0-py<Version>.egg umbennen und damit das .egg in dem Ordner ersetzen
            !!!Vorher ein BACKUP machen!!!
    - Windows:
        Python Pfad ausfindig machen (meistens irgendow in AppData/Local/)
        In \Python\Python311\Lib\site-packages\reachy_sdk die Datei head.py mit der Datei aus dem reachy_sdk zip tauschen

## Robot Movement Script Guide

This is a small Guide on how to use the functions of the Movement-Group

### Available Movement Interface

First, import the required libraries and modules:
(A path to: `/path/to/MoveFacade.py` might be need)

```python
from PythonScripts.Movement.MoveFacade import MoveFacade
from PythonScripts.Movement.Enums.Board import Board
```

The Board Enum class represents the Tic Tac Toe board positions, possible options are:

```python
TOP_LEFT
TOP_CENTER
TOP_RIGHT
CENTER_LEFT 
CENTER
CENTER_RIGHT
BOTTOM_LEFT
BOTTOM_CENTER
BOTTOM_RIGHT
```

Next, create an instance of the MoveFacade class:

```python
move_facade = MoveFacade()
```

### Moving Objects

To move an object, call the `do_move_block()` method of the MoveFacade instance and pass in a value of the Board Enum class:

For Example:

```python
goal_pos = Board.TOP_LEFT # represents a value of (x, y, z)

move_facade.do_move_block(to=goal_pos)
```

## Robot Outside Block Guide

This Guide explains how the available outside block tracking works and how to use it.

### Available Outside Block Interface

First, import the required libraries and modules:
(A path to: `/path/to/OutsideBlockFacade.py` might be need)

```python
from PythonScripts.OutsideBlockFacade import OutsideBlockFacade
```

Next, create an instance of the OutsideBlockFacade class:

```python
block_manager = OutsideBlockFacade()
```

With the help of this interface you can either get or reset the available block count

```python
available_blocks = block_manager.get_block_count() # Get available block count
block_manager.reset() # Reset the block count to the initial state
```

### Important

The available block count will be modified automatically when using the `do_move_block()` using the following interface method:

```python
block_manager.take_block() # Takes a block from the outside and decreases the block availability 
```
