# scale image with the uniform algorithm

import numpy as np

# significantly worse for non-integer factor


def unif_grid(array, factor):
    """
    Scales an image by a factor using uniform using the grid algorithm in uniform distribution. 
    Note: the result is significantly worse for non-integer factors.

    :param array: a numpy array representing the image
    :type file: ndarray
    
    :return: a numpy array representing the scaled image
    :rtype: ndarray
    """
    old_shape = array.shape
    new_arr = np.zeros(
        (int(old_shape[0]*factor), int(old_shape[1]*factor), 3), np.uint8)
    new_shape = new_arr.shape
    for i in range(new_shape[0]):
        for j in range(new_shape[1]):
            for k in range(3):
                new_arr[i][j][k] = array[int(i/factor)][int(j/factor)][k]
    return new_arr
