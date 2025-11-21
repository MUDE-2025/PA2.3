# imports
import pytest
from testbook import testbook
import numpy as np

import justIce


def check_central_diff():
    expected = [0.618, 0.346, 0.423,
                0.222, -0.169, -0.508,
                -0.127, -2.286, 2.540,
                -0.063, -0.169, 0.127,
                -0.169, -1.079]

    # Use dh_dt_CD from justIce.py
    assert np.allclose(justIce.dh_dt_CD, expected, rtol=1e-2), \
        "The central difference calculation is incorrect"

# test for max_even_square.py
import max_even_square

assert max_even_square([3, 7, 2, 8, 5, 10, 6]) == 100, \
       "Function should return the square of the maximum even number"