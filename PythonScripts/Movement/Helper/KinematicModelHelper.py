import numpy
import numpy as np
from enum import Enum
from scipy.spatial.transform import Rotation as R
from numpy import ndarray


class RotationAxis(Enum):
    X = 'x',
    Y = 'y',
    Z = 'z'


class KinematicModelHelper:
    def _build_rot_mat(self, rotation: dict):
        """

        """
        Z = None
        Y = None
        X = None

        for key, value in rotation.items():
            rot = (numpy.around(R.from_euler(key, numpy.deg2rad(value)).as_matrix(), 3))
            if key == 'x':
                X = rot
            if key == 'y':
                Y = rot
            if key == 'z':
                Z = rot

        rotations_combined = np.matmul(Z, Y, X)
        return rotations_combined

    def _build_target_pos_mat(self, rot_mat: ndarray, pose: list):
        """

        :param rot_mat: the rotation matrix
        :param pose: the goal position
        :return: ndarray
        """
        target_pos = []
        for index, mat in enumerate(rot_mat):
            new = numpy.append(mat, pose[index])
            target_pos.append(new)
        target_pos.append([0, 0, 0, 1])
        return numpy.array(target_pos)

    def get_kinematic_move(self, pose: list, rotation: dict):
        rotation_matrix = self._build_rot_mat(rotation)
        return self._build_target_pos_mat(rotation_matrix, pose)
