from utils import printTree

class Node(object):
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

def reconstruct_tree(preorder):
	return reconstruct_tree_(preorder, 0)[0]

def reconstruct_tree_(preorder, i):
	val = preorder[i]
	if val is None:
		return None, i
	node = Node(val)
	node.left, i = reconstruct_tree_(preorder, i+1)
	node.right, i = reconstruct_tree_(preorder, i+1)
	return node, i 

preorder = ['H', 'B', 'F', None, None, 'E', 'A', None, None, None, 'C', None, 'D', None, 'G', 'I', None, None, None]
root = reconstruct_tree(preorder)
printTree(root)
