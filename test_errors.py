# imports
import pytest
from testbook import testbook
import numpy as np

# test for justIce.py
import justIce

# 1. Check the file path fix
assert "auxiliary_files" in file_path, (
    "File path is incorrect. It must point to auxiliary_files/justIce.csv"
)

# 2. Check the central-difference logic fix
assert np.allclose(dh_dt_CD, expected_cd, rtol=1e-2), (
    "Central difference calculation is incorrect. "
    "Make sure your i-loop uses (h[i+1] - h[i]) / (t[i+1] - t[i])."
)

# test for max_even_square.py
import max_even_square

assert max_even_square([3, 7, 2, 8, 5, 10, 6]) == 100, \
       "Function should return the square of the maximum even number"