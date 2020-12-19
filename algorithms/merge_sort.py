from analysis.time_algorithm import time_algorithm

# taken from website: https://www.geeksforgeeks.org/merge-sort/


def merge_sort(A):
    if len(A) > 1:
        mid = len(A) // 2  # Finding the mid of the array
        L = A[:mid]  # Dividing the array elements
        R = A[mid:]  # into 2 halves

        merge_sort(L)  # Sorting the first half
        merge_sort(R)  # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            A[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            A[k] = R[j]
            j += 1
            k += 1


if __name__ == '__main__':
    time_algorithm(merge_sort)
