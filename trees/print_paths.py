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

def print_paths(root):
	print_paths_(root, [])

def print_paths_(root, path):
	if not root:
		return
	path.append(root.val)
	if not root.left and not root.right:
		print path
	else:
		print_paths_(root.left, path)
		print_paths_(root.right, path)
	path.pop()

print_paths(r)
