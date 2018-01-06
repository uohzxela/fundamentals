from utils import printTree
from collections import deque

class Node(object):
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

def reconstruct_tree(preorder):
	preorder = deque(preorder)
	return reconstruct_tree_(preorder)

def reconstruct_tree_(preorder):
	val = preorder.popleft()
	if val is None:
		return None
	node = Node(val)
	node.left = reconstruct_tree_(preorder)
	node.right = reconstruct_tree_(preorder)
	return node

preorder = ['H', 'B', 'F', None, None, 'E', 'A', None, None, None, 'C', None, 'D', None, 'G', 'I', None, None, None]
root = reconstruct_tree(preorder)
printTree(root)
