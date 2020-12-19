# Runtime analysis of sorting algorithms
In this report we look at how Insertion sort, Bubble sort, Merge sort, Quick sort and Tim sort preformes against different list types.


## ABSTRACT
There exists extensive research about the theoretical runtime of
various sorting algorithms. In this paper we investigate real-life
behaviour of quadratic algorithms (Insertion sort and Bubble sort),
sub-quadratic algorithms (Mergesort and Quicksort) and the combined algorithm Timsort. We will also look at Pythons built-in
sorting functions NumPy sort and Python sort. The algorithms are
implemented in Python and tested by sorting various list types
of various sizes. List types we use are increasing list, decreasing
list, random integer list, random float list and string list. The main
result in this paper was that quadratic algorithms had the longest
runtime for sorting lists, with exception of list sizes between 10-40,
where they outperform the sub-quadratic algorithms. The builtin sorting functions outperformed the other algorithms in every
test case. Conclusion of this paper is that all algorithms tested in
this experiment has the same real-life behaviour as the theoretical
performance, except Timsort on increasing lists.
