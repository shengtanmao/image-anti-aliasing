# scale image with the uniform algorithm

import numpy as np
import math as m

# significantly worse for non-integer factor


def unif_grid_2(array, factor):
    """
    Scales an image by a factor using uniform using the grid algorithm in
    uniform distribution.

    :param array: a numpy array representing the image
    :type file: ndarray

    :return: a numpy array representing the scaled image
    :rtype: ndarray
    """
    old_shape = array.shape
    new_arr = np.zeros(
        (round(old_shape[0] * factor), round(old_shape[1] * factor), 3),
        np.uint8)
    new_shape = new_arr.shape
    for i in range(new_shape[0]):
        for j in range(new_shape[1]):
            offset = 2 ** (-10)
            x = i / factor
            x_f = m.floor(x)
            x_c = min(m.ceil(x), old_shape[0] - 1)
            x_f_d = x_f_d = (x - x_f) ** 2 + offset
            x_c_d = (x - x_c) ** 2 + offset

            y = j / factor
            y_f = m.floor(y)
            y_c = min(m.ceil(y), old_shape[1] - 1)
            y_f_d = (y - y_f) ** 2 + offset
            y_c_d = (y - y_c) ** 2 + offset
            weights = [
                1 / (m.sqrt(x_f_d + y_f_d)),
                1 / (m.sqrt(x_c_d + y_c_d)),
                1 / (m.sqrt(x_c_d + y_f_d)),
                1 / (m.sqrt(x_f_d + y_c_d)),
            ]
            for k in range(3):

                new_arr[i][j][k] = (
                    array[x_f][y_f][k] * weights[0]
                    + array[x_c][y_c][k] * weights[1]
                    + array[x_c][y_f][k] * weights[2]
                    + array[x_f][y_c][k] * weights[3]
                ) / sum(weights)
    return new_arr
