from analysis.time_algorithm import time_algorithm

# Got this code from: https://www.geeksforgeeks.org/timsort/

# Python3 program to perform basic timSort
MIN_MERGE = 32


def calc_min_run(n):
    """Returns the minimum length of a
    run from 23 - 64 so that
    the len(array)/minrun is less than or
    equal to a power of 2.

    e.g. 1=>1, ..., 63=>63, 64=>32, 65=>33,
    ..., 127=>64, 128=>32, ...
    """
    r = 0
    while n >= MIN_MERGE:
        r |= n & 1
        n >>= 1
    return n + r


def insertion_sort(A, left, right):
    for i in range(left + 1, right + 1):
        j = i
        while j > left and A[j] < A[j - 1]:
            A[j], A[j - 1] = A[j - 1], A[j]
            j -= 1


# Merge function merges the sorted runs
def merge(A, l, m, r):

    len1, len2 = m - l + 1, r - m
    left, right = [], []
    for i in range(0, len1):
        left.append(A[l + i])
    for i in range(0, len2):
        right.append(A[m + 1 + i])

    i, j, k = 0, 0, l

    while i < len1 and j < len2:
        if left[i] <= right[j]:
            A[k] = left[i]
            i += 1

        else:
            A[k] = right[j]
            j += 1

        k += 1

    # Copy remaining elements of left, if any
    while i < len1:
        A[k] = left[i]
        k += 1
        i += 1

    # Copy remaining element of right, if any
    while j < len2:
        A[k] = right[j]
        k += 1
        j += 1


def tim_sort(A):
    n = len(A)
    minRun = calc_min_run(n)

    for start in range(0, n, minRun):
        end = min(start + minRun - 1, n - 1)
        insertion_sort(A, start, end)
    size = minRun
    while size < n:
        for left in range(0, n, 2 * size):

            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))

            merge(A, left, mid, right)

        size = 2 * size


if __name__ == '__main__':
    time_algorithm(tim_sort)
