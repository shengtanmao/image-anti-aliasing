from src.image_handling import imp
from src.image_handling import imp_unit
import pathlib as pl

images_path = pl.Path('./antialiasing/tests/images')
array=imp_unit(images_path / "triangle.jpeg")

#tests imported image has valid values
def test_valid_value():
    shape=array.shape
    assert(shape[2]==3)
    for i in range(shape[0]):
        for j in range(shape[1]):
            for k in range(shape[2]):
                test_val=array[i][j][k]
                assert test_val<256 and test_val>=0
    
test_valid_value()

#tests imported unit image has valid values
def test_valid_unit():
    shape=array.shape
    assert(shape[2]==3)
    for i in range(shape[0]):
        for j in range(shape[1]):
            for k in range(shape[2]):
                test_val=array[i][j][k]
                assert test_val<1 and test_val>=0
test_valid_unit()
