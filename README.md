# tic-tac-toe

Downloadlink für die aktuelle Unity-Szene mit Reachy, TicTacToe Feld, und roten/grünen Spielfiguren:
    https://gigamove.rwth-aachen.de/en/download/813dc3dff83f48f2163327a79cddf5d7

## Look-At-Fix
Angepasste SDK um die look_at Funktion in der Simulation nutzen zu können.

Nutzung:
    - Für die Arbeit mit der Simulation:
        reachy.head.look_at(x, y, z, duration, "simul")
    - Für die Arbeit mit dem Roboter, falls o.g. nicht funktioniert:
        reachy.head.look_at(x, y, z, duration, "real")
        Das ist der Weg, der in der aktuellen SDK eingeschlagen wird, der zu einem Blocking Error führt

Installation:
    - Linux:
        In /usr/local/lib/python<Version>/site-packages die Datei:
            reachy_sdk-0.7.0-py<Version>.egg durch das hier hochgeladene Archiv ersetzen
            !!!Vorher ein BACKUP machen!!!
    - Windows:
        Python Pfad ausfindig machen (meistens irgendow in AppData/Local/)
        In \Python\Python311\Lib\site-packages\reachy_sdk die Datei head.py mit der Datei aus dem reachy_sdk zip tauschen
            !!!Vorher ein BACKUP machen!!!
