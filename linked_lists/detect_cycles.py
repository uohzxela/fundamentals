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