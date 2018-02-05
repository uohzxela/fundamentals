from utils import printTree, TreeNode

def min_height_bst_from_sorted_array(A):
	if not A:
		return None
	mid = len(A) / 2
	root = TreeNode(A[mid])
	root.left = min_height_bst_from_sorted_array(A[:mid])
	root.right = min_height_bst_from_sorted_array(A[mid+1:])
	return root

printTree(min_height_bst_from_sorted_array([2,3,5,7,11,13,17,19,23]))
