from src.image_handling import imp
import pathlib as pl
import numpy as np

images_path = pl.Path('./antialiasing/tests/images')
array = imp(images_path / "triangle.jpeg")

# test imported image has valid datatype


def test_valid_type():
    assert(array.dtype == np.int16)

# tests imported image has valid array shape


def test_valid_shape():
    shape = array.shape
    assert(shape[0] > 0 and shape[1] > 0 and shape[2] == 3)

# tests imported image has valid values


def test_valid_val():
    shape = array.shape
    for i in range(shape[0]):
        for j in range(shape[1]):
            for k in range(shape[2]):
                test_val = array[i][j][k]
                assert test_val < 256 and test_val >= 0
