class Node (object):
	def __init__(self, val):
		self.val = val
		self.right = None
		self.left = None

def findPaths(root, k):
	if not root: return []
	findPaths_(root, root.val, k, [root.val])

def findPaths_(root, curr, k, res):
	if curr == k:
		print res
		return
	if curr > k: return
	if root.left:
		res.append(root.left.val)
		findPaths_(root.left, curr + root.left.val, k, res)
		res.pop()
	if root.right:
		res.append(root.right.val)
		findPaths_(root.right, curr + root.right.val, k, res)
		res.pop()
	return


r = Node(1)
r.left = Node(7)
r.right = Node(3)
r.left.left = Node(-1)
r.left.right = Node(5)
r.right.left = Node(4)

findPaths(r, -1)

