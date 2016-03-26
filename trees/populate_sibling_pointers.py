class Tree(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
		self.nextRight = None

r = Tree(1)
r.left = Tree(2)
r.right = Tree(3)
r.left.left = Tree(4)
r.left.right = Tree(5)
r.right.left = Tree(6)
r.right.right = Tree(7)

def populate(root):
	if not root: return
	if root.left:
		root.left.nextRight = root.right
	if root.right:
		root.right.nextRight = root.nextRight.left if root.nextRight else None
	populate(root.left)
	populate(root.right)

def printNext(curr):
	while curr is not None:
		print curr.val, "->",
		curr = curr.nextRight
	print "None"

populate(r)

printNext(r)
printNext(r.left)
printNext(r.left.left)
