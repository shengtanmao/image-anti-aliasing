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
    return np.asarray(im.open(file))


def exp(array, file):
    """
    Exports an a numpy array and saves it as the file indicated.

    :param array: a three dimesional numpy array representing the image
    :type array: ndarray

    :param file: file path
    :type file: string
    """
    im.fromarray(array).save(file)
