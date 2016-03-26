class Tree(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

r = Tree(10)
r.left = Tree(5)
r.right = Tree(15)
r.right.left = Tree(6)
r.right.right = Tree(20)

r2 = Tree(10)
r2.left = Tree(5)
r2.right = Tree(15)
r2.right.left = Tree(11)
r2.right.right = Tree(20)

def isBST_(root, l, r):
	if not root: return True
	if root.val < l or root.val > r: return False
	return isBST_(root.left, l, root.val) and isBST_(root.right, root.val, r)

def isBST(root):
	return isBST_(root, float('-inf'), float('inf'))

print isBST(r)
print isBST(r2)