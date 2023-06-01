import numpy
from numpy import ndarray
from scipy.spatial.transform import Rotation as R


class KinematicModelHelper:

    def _calculate_rot_mat(self, direction: str, deg: int):
        return numpy.around(R.from_euler(direction, numpy.deg2rad(deg)).as_matrix(), 3)

    def _build_rot_mat(self, rotation: dict):
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
