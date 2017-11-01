class Heap(object):
    def __init__(self):
        self.arr = []
        self.size = 0
        self.CAPACITY = 1000

    def heapify(self, arr):
        """
        Time complexity: O(n)

        arr is an array with arbitrarily placed elements.
        The observation is that any element that is indexed
        after (self.size/2)-1 is a leaf node.
        Hence, it is an one-element heap from that point onward,
        so we only need to bubble down the non-leaf nodes before that index.
        """
        self.arr = arr
        self.size = len(arr)
        for i in xrange(self.size/2-1, -1, -1):
            self.__bubble_down(i)

    def insert(self, val):
        """Time complexity: O(log n)"""
        if self.size >= self.CAPACITY:
            print 'Warning: heap is full'
            return False
        self.arr.append(val)
        self.__bubble_up(self.size)
        self.size += 1
        return True

    def __bubble_up(self, i):
        """Time complexity: O(log n)"""
        parent = (i-1)/2
        if parent < 0:
            return
        if self.arr[i] < self.arr[parent]:
            self.__swap(parent, i)
            self.__bubble_up(parent)

    def __bubble_down(self, i):
        """Time complexity: O(log n)"""
        left = i*2+1
        right = i*2+2
        min_idx = i

        if left < self.size and self.arr[left] < self.arr[min_idx]:
            min_idx = left
        if right < self.size and self.arr[right] < self.arr[min_idx]:
            min_idx = right
        if min_idx != i:
            self.__swap(min_idx, i)
            self.__bubble_down(min_idx)

    def extract_min(self):
        """Time complexity: O(log n)"""
        min_val = self.get_min()
        if min_val is None:
            return None
        self.__swap(0, self.size-1)
        self.size -= 1
        self.__bubble_down(0)
        return min_val

    def get_min(self):
        """Time complexity: O(1)"""
        if self.size <= 0:
            print 'Warning: heap is empty'
            return None
        return self.arr[0]

    def __swap(self, i, j):
        self.arr[i], self.arr[j] = self.arr[j], self.arr[i]

heap = Heap()

assert heap.extract_min() is None

heap.insert(3)
heap.insert(2)
heap.insert(15)
heap.insert(5)
heap.insert(4)
heap.insert(45)

assert heap.extract_min() == 2
assert heap.extract_min() == 3
assert heap.extract_min() == 4
assert heap.extract_min() == 5
assert heap.extract_min() == 15
assert heap.extract_min() == 45
assert heap.extract_min()is None

heap2 = Heap()
heap2.heapify([3, 45, 15, 5, 4, 2])
assert heap2.arr == [2, 4, 3, 5, 45, 15]
