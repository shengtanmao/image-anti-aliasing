from src.image_handling import imp
from src.supersampling.uniform_grid import unif_grid
import pathlib as pl
import numpy as np
from pytest import mark

images_path = pl.Path('./antialiasing/tests/images')
array=imp(images_path / "triangle.jpeg")
shape=array.shape

@mark.parametrize("image,factor",[(array,2),(array,0.4),(array,1.7),(array,0.3)])
def test_unif_grid(image,factor):
    new_arr=unif_grid(image,factor)
    new_shape=new_arr.shape
    assert(int(shape[0]*factor)==new_shape[0] and int(shape[1]*factor)==new_shape[1] and new_shape[2]==3)
    assert(new_arr.dtype==np.uint8)
    for i in range(new_shape[0]):
        for j in range(new_shape[1]):
            for k in range(shape[2]):
                test_val=new_arr[i][j][k]
                assert test_val<256 and test_val>=0

test_unif_grid(array,0.3)