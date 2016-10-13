def sum_root_to_leaf_paths(root):
	return sum_paths(root, 0)

def sum_paths(root, res):
	if not root:
		return 0
	res = res*2+root.val
	if not root.left and not root.right:
		return res
	left = sum_paths(root.left, res)
	right = sum_paths(root.right, res)
	return left + right

class Node(object):
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

n = Node(1)
n.left = Node(0)
n.right = Node(1)

n.left.left = Node(0)
n.left.right = Node(1)

n.left.left.left = Node(0)
n.left.left.right = Node(1)

n.left.right.right = Node(1)
n.left.right.right.left = Node(0)

n.right.left = Node(0)
n.right.right = Node(0)
n.right.left.right = Node(0)
n.right.left.right.left = Node(1)
n.right.left.right.right = Node(0)
n.right.left.right.left.right = Node(1)

n.right.right.right = Node(0)

assert sum_root_to_leaf_paths(n) == 126