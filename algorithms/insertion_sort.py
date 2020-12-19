from analysis.time_algorithm import time_algorithm


def insertion_sort(A):
    """
    Python implementation of insertion sort  
    """
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i -= 1
        A[i + 1] = key


if __name__ == '__main__':
    time_algorithm(insertion_sort)
