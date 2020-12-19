from analysis.time_algorithm import time_algorithm


def bubble_sort(A):
    """
    Python implementation of bubble sort
    """
    length = len(A)
    for i in range(length - 1):
        for j in range(1, length - i):
            if A[j] < A[j - 1]:
                A[j], A[j-1] = A[j-1], A[j]


if __name__ == '__main__':
    time_algorithm(bubble_sort)
