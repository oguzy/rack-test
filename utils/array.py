import numpy as np
from StringIO import StringIO


class ArrayOps:

    def __init__(self):
        self.array_object = None

    def set_array(self, array_object):
        self.array_object = array_object

    def get_array(self):
        return self.array_object

    def print_in_clock_wise(self):
        """
        :param start_row_index: starting row index
        :param end_row_index: ending row index
        :param start_column_index: starting column index
        :param end_column_index: ending column index
        :param i:  iterator
        """

        arr = self.get_array()

        if arr.size == 1:
            print arr
            return True

        if arr.size == 2:
            print arr[0], arr[1]
            return True

        if arr.size == 4:
            print arr[0][0], arr[0][1], \
                    arr[1][1], arr[1][0]
            return True

        m = arr.shape[0]
        n = arr.shape[1]

        start_row_index = 0
        end_row_index = m
        start_column_index = 0
        end_column_index = n

        result = []

        while start_row_index < end_row_index and start_column_index < end_column_index:
            #Print the first row
            for i in xrange(start_column_index, end_column_index, 1):
                result.append(arr[start_row_index][i])

            start_row_index += 1

            #Print the last column
            for i in xrange(start_row_index, end_row_index, 1):
                result.append(arr[i][end_column_index-1])

            end_column_index -= 1

            #Print the last row from remaining ones
            if start_row_index < end_row_index:
                for i in xrange(end_column_index-1, 0, -1):
                    result.append(arr[end_row_index-1][i])

                end_row_index -= 1

            #Print the first column from remaining ones
            if start_column_index < end_column_index:
                for i in xrange(end_row_index, 0, -1):
                    if arr[i][start_column_index] in result:
                        break
                    result.append(arr[i][start_column_index])

                start_column_index += 1

        print " ".join(map(str, result))
        return True

    def create_array(self, f):
        """
        :param f: File to be read, with full path, each line should be defining each row of the array
                    with space separated
        :return:  2D array
        """
        input_f = None
        try:
            input_f = open(f)
        except IOError as e:
            print ("({})".format(e))
            return np.array([[]])

        s_obj = StringIO(input_f.read())
        return np.loadtxt(s_obj, dtype=int)





