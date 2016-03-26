class Tree(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

r = Tree(5)
r.left = Tree(1)
r.right = Tree(5)
r.left.left = Tree(5)
r.left.right = Tree(5)
r.right.right = Tree(5)

count = 0

def unival(root):
	global count
	count = 0
	unival_(root)
	print count


# def unival_(root):
# 	if not root: return True
# 	isLeftUnival = unival_(root.left)
# 	isRightUnival = unival_(root.right)
# 	global count
# 	if isLeftUnival and isRightUnival:
# 		if not root.right and not root.left:
# 			count += 1
# 			return True
# 		if not root.right and root.left.val == root.val:
# 			count += 1
# 			return True
# 		if not root.left and root.right.val == root.val:
# 			count += 1
# 			return True
# 		if root.right.val == root.val and root.left.val == root.val:
# 			count += 1
# 			return True
# 	return False

def unival_(root):
	if not root: return True
	isLeftUnival = unival_(root.left)
	isRightUnival = unival_(root.right)
	global count
	if isLeftUnival and isRightUnival:
		# shortened implementation
		if ((root.right and root.right.val != root.val) or
			(root.left and root.left.val != root.val)):
			return False
		count += 1
		return True
	return False

unival(r)