import numpy
from numpy import ndarray
from scipy.spatial.transform import Rotation as R


class KinematicModelHelper:
    """
    Die KinematicModelHelper-Klasse bietet Hilfsfunktionen zur Berechnung des kinematischen Modells des Reachy-Roboters.

    Methods:
        _calculate_rot_mat(direction: str, deg: int) -> ndarray:
            Berechnet die Rotationsmatrix für die gegebene Richtung und den gegebenen Winkel.

        _build_rot_mat(rotation: dict) -> ndarray:
            Erstellt die Rotationsmatrix aus den gegebenen Rotationswerten.

        _build_target_pos_mat(rot_mat: ndarray, pose: list) -> ndarray:
            Erstellt die Zielpositions-Matrix aus der Rotationsmatrix und der Zielposition.

        get_kinematic_move(pose: list, rotation: dict) -> ndarray:
            Gibt die kinematische Bewegung basierend auf der Zielposition und der Rotation zurück.
    """

    def _calculate_rot_mat(self, direction: str, deg: int):
        """
        Berechnet die Rotationsmatrix für die gegebene Richtung und den gegebenen Winkel.

        Args:
            direction (str): Die Richtung der Rotation ('x', 'y' oder 'z').
            deg (int): Der Rotationswinkel in Grad.

        Returns:
            ndarray: Die berechnete Rotationsmatrix.
        """
        return numpy.around(R.from_euler(direction, numpy.deg2rad(deg)).as_matrix(), 3)

    def _build_rot_mat(self, rotation: dict):
        """
        Erstellt die Rotationsmatrix aus den gegebenen Rotationswerten.

        Args:
            rotation (dict): Ein Wörterbuch, das die Rotationswerte für die Richtungen 'x', 'y' und 'z' enthält.

        Returns:
            ndarray: Die erstellte Rotationsmatrix.
        """
        Z = None
        Y = None
        X = None

        for key, value in rotation.items():
            rot = self._calculate_rot_mat(key, value)
            if key == 'x':
                X = rot
            if key == 'y':
                Y = rot
            if key == 'z':
                Z = rot

        rotations_combined = numpy.matmul(Z, Y, X)
        return rotations_combined

    def _build_target_pos_mat(self, rot_mat: ndarray, pose: list):
        """
        Erstellt die Zielpositions-Matrix aus der Rotationsmatrix und der Zielposition.

        Args:
            rot_mat (ndarray): Die Rotationsmatrix.
            pose (list): Die Zielposition als Liste von Koordinaten.

        Returns:
            ndarray: Die erstellte Zielpositions-Matrix.
        """
        target_pos = []
        for index, mat in enumerate(rot_mat):
            new = numpy.append(mat, pose[index])
            target_pos.append(new)
        target_pos.append([0, 0, 0, 1])
        return numpy.array(target_pos)

    def get_kinematic_move(self, pose: list, rotation: dict):
        """
        Gibt die kinematische Bewegung basierend auf der Zielposition und der Rotation zurück.

        Args:
            pose (list): Die Zielposition als Liste von Koordinaten.
            rotation (dict): Ein Wörterbuch, das die Rotationswerte für die Richtungen 'x', 'y' und 'z' enthält.

        Returns:
            ndarray: Die kinematische Bewegung als Zielpositions-Matrix.
        """
        rotation_matrix = self._build_rot_mat(rotation)
        return self._build_target_pos_mat(rotation_matrix, pose)
