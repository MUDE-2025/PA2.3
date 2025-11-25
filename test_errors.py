# imports
import numpy as np

import max_even_square

def test_max_even_square():
    """Test that max_even_square returns the square of the maximum even number."""
    assert max_even_square.max_even_square([3, 7, 2, 8, 5, 10, 6]) == 100, \
        "Function should return the square of the maximum even number"
