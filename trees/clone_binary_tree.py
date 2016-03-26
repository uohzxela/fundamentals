class Tree(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

r = Tree(1)
r.left = Tree(2)
r.right = Tree(3)
r.left.left = Tree(4)
r.left.right = Tree(5)
r.right.left = Tree(6)
r.right.right = Tree(7)

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

def clone(root):
	if not root: return None
	r = Tree(root.val)
	r.left = clone(root.left)
	r.right = clone(root.right)
	return r 

print_level(r)
print_level(clone(r))