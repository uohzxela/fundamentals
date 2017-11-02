from ..data_structures.heap import Heap

# cd one level up fundamentals directory and python -m fundamentals.sorting.heapsort


def make_heap(A):
    heap = Heap()
    for i in xrange(len(A)):
        heap.insert(A[i])
    return heap


def heapsort(A):
    heap = make_heap(A)
    for i in xrange(len(A)):
        A[i] = heap.extract_min()

A = [23, 21, 5, 9, 10, 1, 8, 3, 0, -1, -10]
sorted_A = sorted(A)
heapsort(A)
assert A == sorted_A
