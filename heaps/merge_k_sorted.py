# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from heapq import *
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        dummy = curr = ListNode(0)
        heap = []
        for node in lists:
            if not node: continue
            heappush(heap, (node.val, node))
        
        while heap and heap[0][0] != float('inf'):
            _, node = heappop(heap)
            curr.next = node
            curr = curr.next
            heappush(heap,
                     (node.next.val if node.next else float('inf'),
                      node.next))
            
        return dummy.next
