import numpy

from scipy.spatial.transform import Rotation as R
from numpy import ndarray


class KinematicModelHelper:
    def get_rot_mat(self, rot_direction: str, rot_axis: int):
        """

        :param rot_direction: the rotation axis
        :param rot_axis: the rotation amount around the axis
        :return: ndarray
        """
        return numpy.around(R.from_euler(rot_direction, numpy.deg2rad(rot_axis)).as_matrix(), 3)

    def get_target_pos_mat(self, rot_mat: ndarray, pos: list):
        """

        :param rot_mat: the rotation matrix
        :param pos: the goal position
        :return: ndarray
        """
        target_pos = []
        for index, mat in enumerate(rot_mat):
            new = numpy.append(mat, pos[index])
            target_pos.append(new)
        target_pos.append([0, 0, 0, 1])
        return numpy.array(target_pos)
