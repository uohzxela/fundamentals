def detectCycles(head):
	slow = fast = head
	while fast and fast.next:
		fast = fast.next.next
		slow = slow.next
		if fast == slow: return True
	return False

"""Easier to ask for forgiveness than permission."""
def hasCycle(head):
    try:
        slow = head
        fast = head.next
        while slow is not fast:
            slow = slow.next
            fast = fast.next.next
        return True
    except:
        return False

# returns start of cycle if any
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = fast = head
        has_cycle = False
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                has_cycle = True
                break
        if not has_cycle:
            return None
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow
