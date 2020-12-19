from analysis.time_algorithm import time_algorithm

import numpy as np


def numpy_sort(A):
    np.sort(A)


def python_sort(A):
    A.sort()


if __name__ == '__main__':
    #time_algorithm(python_sort)
    time_algorithm(numpy_sort)
