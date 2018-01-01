class Node(object):
	def __init__(self, data=0, next_node=None):
		self.data = data
		self.next = next_node

def remove(L, k):
	dummy = Node(0, L)
	p1 = dummy.next
	for _ in xrange(k):
		p1 = p1.next
	p2 = dummy
	while p1:
		p1, p2 = p1.next, p2.next
	# p2 is now at (k+1)th last node
	p2.next = p2.next.next
	return dummy.next

L = Node(0)
L.next = Node(1)
L.next.next = Node(2) # 0 -> 1 -> 2

L = remove(L, 3) # remove first node: 1 -> 2
assert L.data == 1 # 1 -> 2
L = remove(L, 1) # remove last node: 1
assert L.data == 1 # 2
