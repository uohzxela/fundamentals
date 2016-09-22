def has_path_sum(root, target):
	return has_path_sum_(root, target, 0)

def has_path_sum_(root, target, res):
	if not root: return False
	res += root.val
	if root.left is None and root.right is None:
		return res == target
	# we are only finding if a root-to-leaf path has target sum, not summing up all the paths
	# hence we return a boolean value (contrast this with sum_root_to_leaf_paths.py)
	return (has_path_sum_(root.left, target, res) or 
			has_path_sum_(root.right,target, res))

class Node(object):
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

r = Node(314)
r.left = Node(6)
r.left.left = Node(271)
r.left.left.left = Node(28)
r.left.left.right = Node(0)

r.left.right = Node(561)
r.left.right.right = Node(3)
r.left.right.right.left = Node(17)

r.right = Node(6)
r.right.left = Node(2)
r.right.left.right = Node(1)
r.right.left.right.left = Node(401)
r.right.left.right.right = Node(257)
r.right.left.right.left.right = Node(641)

r.right.right = Node(271)
r.right.right.right = Node(28)

assert has_path_sum(r, 591)