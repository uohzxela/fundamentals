import collections
from utils import TreeNode

Interval = collections.namedtuple('Interval', ('left', 'right'))

def range_lookup_in_bst(root, interval):
	def helper(root):
		if not root:
			return
		if interval.left <= root.val <= interval.right:
			helper(root.left)
			res.append(root.val)
			helper(root.right)
		elif interval.left > root.val:
			helper(root.right)
		else:
			helper(root.left)
	res = []
	helper(root)
	return res

root = TreeNode(19)
root.left = TreeNode(7)
root.left.left = TreeNode(3)
root.left.left.left = TreeNode(2)
root.left.left.right = TreeNode(5)

root.left.right = TreeNode(11)
root.left.right.right = TreeNode(17)
root.left.right.right.left = TreeNode(13)

root.right = TreeNode(43)
root.right.left = TreeNode(23)
root.right.left.right = TreeNode(37)
root.right.left.right.left = TreeNode(29)
root.right.left.right.left.right = TreeNode(31)
root.right.left.right.right = TreeNode(41)

root.right.right = TreeNode(47)
root.right.right.right = TreeNode(53)

assert range_lookup_in_bst(root, Interval(16, 31)) == [17, 19, 23, 29, 31]
