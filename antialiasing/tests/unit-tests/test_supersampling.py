from src.image_handling import imp
from src.supersampling.uniform_grid import unif_grid
import pathlib as pl
import numpy as np

images_path = pl.Path('./antialiasing/tests/images')
array=imp(images_path / "triangle.jpeg")
shape=array.shape

def test_unif_grid_shape():
    factor=1.5
    new_arr=unif_grid(array,factor)
    new_shape=new_arr.shape
    assert(int(shape[0]*factor)==new_shape[0] and int(shape[1]*factor)==new_shape[1] and new_shape[2]==3)
    
def test_unit_grid_type():
    new_arr=unif_grid(array,1.5)
    assert(new_arr.dtype==np.uint8)

def test_unit_grid_val():
    new_arr=unif_grid(array,1.5)
    new_shape=new_arr.shape
    for i in range(new_shape[0]):
        for j in range(new_shape[1]):
            for k in range(shape[2]):
                test_val=new_arr[i][j][k]
                assert test_val<256 and test_val>=0