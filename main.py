#!/bin/python

import os
from utils.array import ArrayOps


#put your filename here
#it is assume that the file is at the same directory
file_name = "test.txt"
file_path = os.path.join(os.getcwd(), file_name)

arr = ArrayOps()
two_d_arr = arr.create_array(file_path)
if two_d_arr.any():
    arr.set_array(two_d_arr)
    arr.print_in_clock_wise()