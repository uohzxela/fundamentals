class Tree(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

r = Tree(30)
r.left = Tree(10)
r.left.left = Tree(50)
r.right = Tree(20)
r.right.left = Tree(45)
r.right.right = Tree(35)

r2 = Tree(30)
r2.left = Tree(20)
r2.left.left = Tree(10)
r2.left.left.left = Tree(5)
r2.left.left.right = Tree(15)
r2.left.right = Tree(25)
r2.left.right.right = Tree(28)
r2.right = Tree(40)
r2.right.left = Tree(35)
r2.right.right = Tree(50)
r2.right.right.left = Tree(41)

def isLeaf(root):
	return not root.left and not root.right

def printLeftBoundaryAndLeaves(root, isBoundary):
	if not root: return
	if isBoundary or isLeaf(root):
		print root.val,
	printLeftBoundaryAndLeaves(root.left, isBoundary)
	printLeftBoundaryAndLeaves(root.right, isBoundary and not root.left)

def printRightBoundaryAndLeaves(root, isBoundary):
	if not root: return
	printRightBoundaryAndLeaves(root.left, isBoundary and not root.right)
	printRightBoundaryAndLeaves(root.right, isBoundary)
	if isBoundary or isLeaf(root):
		print root.val,

def printExterior(root):
	if not root: return
	print root.val,
	printLeftBoundaryAndLeaves(root.left, True)
	printRightBoundaryAndLeaves(root.right, True)

printExterior(r2)

