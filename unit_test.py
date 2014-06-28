import random
import unittest
import numpy as np
from utils.array import ArrayOps


class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.arr = np.random.randint(5, size=(random.randint(1, 10), random.randint(1, 10)))

    def test_print_in_clock_wise(self):
        arr_class = ArrayOps()
        arr_class.set_array(self.arr)
        self.assertTrue(arr_class.print_in_clock_wise())

if __name__ == '__main__':
    unittest.main()