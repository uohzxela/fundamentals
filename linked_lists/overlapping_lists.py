# Write a program to find the node at which the intersection of two singly linked lists begins.
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        def length(L):
            length = 0
            while L:
                length += 1
                L = L.next
            return length

        len1, len2 = length(headA), length(headB)
        p1, p2 = headA, headB
        
        # advances thru the longer list
        while len1 > len2:
            p1, len1 = p1.next, len1 - 1
        while len2 > len1:
            p2, len2 = p2.next, len2 - 1

        while p1 and p1 != p2:
            p1, p2 = p1.next, p2.next
        return p1
