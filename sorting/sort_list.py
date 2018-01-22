# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        slow, fast, pre_slow = head, head, None

        while fast and fast.next:
            pre_slow = slow
            slow = slow.next
            fast = fast.next.next
        pre_slow.next = None

        return self.merge(self.sortList(head), self.sortList(slow))
    
    def merge(self, left, right):
        curr = dummy = ListNode(0)
        
        while left and right:
            if left.val <= right.val:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next
            curr = curr.next
        
        if left: curr.next = left
        if right: curr.next = right
            
        return dummy.next
