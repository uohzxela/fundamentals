from utils import printTree
from collections import deque

class TreeNode(object):
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

def rebuild_bst_from_preorder(preorder_seq):
	if not preorder_seq:
		return None
	# second arg is used when iterator is exhausted
	transition_point = next((i for i, a in enumerate(preorder_seq) if a > preorder_seq[0]), len(preorder_seq))

	root = TreeNode(preorder_seq[0])
	root.left = rebuild_bst_from_preorder(preorder_seq[1:transition_point])
	root.right = rebuild_bst_from_preorder(preorder_seq[transition_point:])

	return root

def rebuild_bst_from_preorder2(preorder_seq):
	def helper(left, right):
		if not preorder:
			return None
		if not left <= preorder[0] <= right:
			return None
		root = TreeNode(preorder[0])
		preorder.popleft()
		root.left = helper(left, root.val)
		root.right = helper(root.val, right)
		return root

	preorder = deque(preorder_seq)
	return helper(float('-inf'), float('inf'))


preorder_seq = [43, 23, 37, 29, 31, 41, 47, 53]
printTree(rebuild_bst_from_preorder(preorder_seq))
print '----------------------------------'
printTree(rebuild_bst_from_preorder2(preorder_seq))
