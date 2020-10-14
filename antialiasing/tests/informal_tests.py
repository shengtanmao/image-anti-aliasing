from src.image_handling import *
from src.supersampling.uniform_grid import *
import pathlib as pl

images_path = pl.Path('./antialiasing/tests/images')

image=imp(images_path / "2017-Rolls-Royce-Wraith-012-2160.jpg")
modified=unif_grid(image,2)
exp(modified,images_path / "rr.jpg",)