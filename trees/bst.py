from utils import printTree

class TreeNode(object):
	def __init__(self, val):
		self.val = val
		self.right = None
		self.left = None

class BST(object):
	def __init__(self):
		self.root = None

	def insert(self, val):
		self.root = self.insert_(self.root, val)

	def insert_(self, root, val):
		if not root: return TreeNode(val)
		if root.val < val:
			root.right = self.insert_(root.right, val)
		else:
			root.left = self.insert_(root.left, val)
		return root

	def replace_node(self, parent, old_child, new_child):
		# if parent is null, that means old_child is the root
		# replace root with new_child
		if not parent:
			self.root = new_child
			return
		if parent.left == old_child:
			parent.left = new_child
		else:
			parent.right = new_child

	def find_target(self, val):
		target, target_parent = self.root, None
		while target and target.val != val:
			target_parent = target
			target = target.left if target.val > val else target.right
		return target, target_parent

	def find_successor(self, root):
		successor, successor_parent = root.right, root
		while successor.left:
			successor_parent = successor
			successor = successor.left
		return successor, successor_parent

	def delete(self, val):
		print "deleting", val, "..."
		target, target_parent = self.find_target(val)
		if not target: 
			return False

		# if target node has a right child, replace it with its successor
		if target.right:
			successor, successor_parent = self.find_successor(target)

			# replace successor with its right child
			# why not left child? because its left child pointer is always empty
			self.replace_node(parent=successor_parent, 
							  old_child=successor, 
							  new_child=successor.right)

			 # replace target node with its successor
			self.replace_node(parent=target_parent, 
							  old_child=target, 
							  new_child=successor)

			# set successor's left child to target node's left child 
			successor.left = target.left
			# set successor's right child to target node's right child
			# only if successor's parent is not the target node
			if target.right != successor:
				successor.right = target.right

		# if target node has no successor, replace it with its left child
		else:
			self.replace_node(parent=target_parent,
							  old_child=target,
							  new_child=target.left)

		return True
				

bst = BST()
bst.insert(7)
bst.insert(5)
bst.insert(9)
bst.insert(8)
bst.insert(8.5)
bst.insert(3)
bst.insert(6)
bst.insert(10)
bst.insert(15)
bst.insert(13)
bst.insert(2)
bst.insert(1)

print "before delete"
printTree(bst.root)

# bst.delete(5)
bst.delete(7)

printTree(bst.root)
