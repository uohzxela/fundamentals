class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy1, dummy2 = ListNode(0), ListNode(0)
        tails, turn = [dummy1, dummy2], 0
        
        while head:
            tails[turn].next = head
            tails[turn] = tails[turn].next
            turn ^= 1 # alternate between even and odd
            head = head.next

        tails[1].next = None
        tails[0].next = dummy2.next

        return dummy1.next
