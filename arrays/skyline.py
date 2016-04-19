import heapq

'''
3 ways to solve:
1. use height map, O(n^2)
2. use a heap, O(nlogn)
    1. append edge (x-coordinate, height) to an array, use isStart to mark if it's left or right edge
    2. sort edges by x-coordinate
    3. initialize a max heap to store edge heights
    3. iterate over the sorted edges,
        for each edge, 
            if it's a left edge
                if heap is empty or its height > heap.peek()
                    add it to result
                add edge height to heap
            otherwise 
                remove height of its left edge (same as right edge) from heap
                if heap is empty
                    add to result as edge with 0 height
                else if its height > heap.peek()
                    add to result as-is
3. use divide and conquer, variant of mergesort
'''

class Strip(object):
    def __init__(self, x, h, isStart):
        self.x = x
        self.h = h
        self.isStart = isStart

class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        strips = []
        for b in buildings:
            x1, h, x2 = b
            strips.append(Strip(x1, h, True))
            strips.append(Strip(x2, h, False))

        strips.sort(key = lambda strip: strip.x)

        heap = []
        res = []

        for s in strips:
            if s.isStart:
                if not heap or s.h > heap[-1]:
                    res.append([s.x, s.h])
                heapq.heappush(heap, s.h)
            else:
                '''
                O(N) operation (heapify and find index), making this algorithm O(N^2)
                therefore couldn't pass test cases on Leetcode due to TLE
                need a dictionary to point to index to find it in O(1) time, 
                and use O(logn) operation to remove item from heap
                '''
                heap[heap.index(s.h)] = heap[-1]
                heap.pop()
                heapq.heapify(heap)
                if not heap:
                    res.append([s.x, 0])
                elif heap[-1] < s.h:
                    res.append([s.x, heap[-1]])
        return res


print Solution().getSkyline([[1,11,5],[2,6,7],[3,13,9],[12,7,16],[14,3,25],[19,18,22],[23,13,29],[24,4,28]])