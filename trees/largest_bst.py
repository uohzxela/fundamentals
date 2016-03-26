class Tree(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

r = Tree(15)
r.left = Tree(10)
r.right = Tree(20)
r.left.left = Tree(5)
r.left.right = Tree(7)
r.left.right.left = Tree(2)
r.left.right.left.left = Tree(0)
r.left.right.left.right = Tree(8)
r.left.right.right = Tree(5)
r.left.right.right.left = Tree(3)

max_size = 0
largest_bst = None

def print_level(root):
	if not root: return
	q = [root]
	while q:
		curr_len = len(q)
		for _ in xrange(curr_len):
			n = q.pop(0)
			if n.left: q.append(n.left)
			if n.right: q.append(n.right)
			print n.val,
		print

def largestBST(root):
	largestBST_(root, float('-inf'), float('inf'))
	print_level(largest_bst)

def largestBST_(root, l, h):
	if not root: return 0, None
	if root.val <= l or root.val >= h:
		largestBST_(root, float('-inf'), float('inf'))
		return 0, None
	curr_node = Tree(root.val)
	left_size, left_bst = largestBST_(root.left, l, root.val)
	right_size, right_bst = largestBST_(root.right, root.val, h)

	curr_node.left = left_bst
	curr_node.right = right_bst

	curr_size = left_size + right_size + 1

	global max_size, largest_bst
	if curr_size > max_size:
		max_size = curr_size
		largest_bst = curr_node
	return curr_size, curr_node

largestBST(r)