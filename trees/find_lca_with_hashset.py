def lca(node0, node1):
	hset = set()
	while node0 or node1:
		if node0:
			if node0 in hset:
				return node0
			hset.add(node0)
			node0 = node0.parent
		if node1:
			if node1 in hset:
				return node1
			hset.add(node1)
			node1 = node1.parent
	raise Exception("node0 and node1 are not in the same tree.")


class Node(object):
	def __init__(self, val):
		self.val = val
		self.parent = None
		self.left = None
		self.right = None

"""
   1
 /   \
2     3
	 /  \
    4    5
    	/
       6	
"""

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)

node1.left = node2
node2.parent = node1
node1.right = node3
node3.parent = node1

node3.left = node4
node4.parent = node3
node3.right = node5
node5.parent = node3

node5.left = node6
node6.parent = node5


assert lca(node6, node4) == node3
assert lca(node6, node3) == node3
assert lca(node6, node2) == node1
try:
	assert lca(Node(7), node1)
except Exception as e: 
	print e.message
