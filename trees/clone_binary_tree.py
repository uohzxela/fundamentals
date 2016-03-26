from utils import printTree

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

def clone(root):
	if not root: return None
	r = Tree(root.val)
	r.left = clone(root.left)
	r.right = clone(root.right)
	return r 

printTree(r)
printTree(clone(r))