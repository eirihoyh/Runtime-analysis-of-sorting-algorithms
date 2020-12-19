from analysis.time_algorithm import time_algorithm


# quick sort, found pseudocode in L07 and used that to make both functions
def partition(A, p, r):
    x = A[r]
    i = p-1
    for j in range(p, r):
        if A[j] <= x:
            i = i+1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i + 1


def quick_sort(A, p=0, r=None):
    if r == None:
        r = len(A)-1
    if p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q-1)
        quick_sort(A, q+1, r)


if __name__ == '__main__':
    time_algorithm(quick_sort)
