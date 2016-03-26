class Tree(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

r = Tree(6)
r.left = Tree(3)
r.right = Tree(4)
r.left.left = Tree(7)
r.left.right = Tree(3)
r.right.left = Tree(8)
r.right.right = Tree(1)

def flip(root):
	if not root: return
	root.left, root.right = root.right, root.left 
	flip(root.left)
	flip(root.right)

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

print_level(r)
flip(r)
print_level(r)