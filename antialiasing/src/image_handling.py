# functions for importing and exporting images
import PIL.Image as im
import numpy as np


def imp(file):
    """
    Imports an image as a numpy array.

    :param file: file path
    :type file: string

    :return: a three dimesional numpy array representing the image
    :rtype: ndarray
    """
    return np.asarray(im.open(file), dtype=np.int16)


def exp(array, file):
    """
    Exports an a numpy array and saves it as the file indicated.

    :param array: a three dimesional numpy array representing the image
    :type array: ndarray

    :param file: file path
    :type file: string
    """
    im.fromarray(array.astype(np.uint8)).save(file)


def score(old, new):
    """
    Scores two images of same dimensions on similarity from 0 to 255.
    The smaller the score the more similar they are.

    :param old: a three dimesional numpy array representing the image
    :type array: ndarray

    :param new: a three dimesional numpy array representing the image
    :type array: ndarray

    :return: score from 0 to 255
    :rtype: double
    """
    assert(old.shape[0] == new.shape[0] and old.shape[1] == new.shape[1])
    sum = 0
    for i in range(new.shape[0]):
        for j in range(new.shape[1]):
            for k in range(3):
                sum += abs(new[i][j][k] - old[i][j][k])
    return sum/(new.shape[0]*new.shape[1]*3)
