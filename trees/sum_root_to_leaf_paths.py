def sum_root_to_leaf_paths(root):
	return dfs(root, 0)

def dfs(root, res):
	if not root: return 0
	res = res*2+root.val
	if not root.l and not root.r:
		return res
	left = dfs(root.l, res)
	right = dfs(root.r, res)
	return left + right

class Node(object):
	def __init__(self, val):
		self.val = val
		self.l = None
		self.r = None

n = Node(1)
n.l = Node(0)
n.r = Node(1)

n.l.l = Node(0)
n.l.r = Node(1)

n.l.l.l = Node(0)
n.l.l.r = Node(1)

n.l.r.r = Node(1)
n.l.r.r.l = Node(0)

n.r.l = Node(0)
n.r.r = Node(0)
n.r.l.r = Node(0)
n.r.l.r.l = Node(1)
n.r.l.r.r = Node(0)
n.r.l.r.l.r = Node(1)

n.r.r.r = Node(0)

assert sum_root_to_leaf_paths(n) == 126