class Node(object):
	def __init__(self, data=0, next_node=None):
		self.data = data
		self.next = next_node

def merge(L1, L2):
	dummy = curr = Node()

	while L1 and L2:
		if L1.data <= L2.data:
			curr.next = L1
			L1 = L1.next
		else:
			curr.next = L2
			L2 = L2.next
		curr = curr.next

	curr.next = L1 or L2
	return dummy.next

L1 = Node(0)
L1.next = Node(2)
L1.next.next = Node(4)

L2 = Node(1)
L2.next = Node(3)
L2.next.next = Node(5)
L2.next.next.next = Node(6)

merged = merge(L1, L2)
for i in xrange(7):
	assert merged.data == i
	merged = merged.next
