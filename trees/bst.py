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

	def min(self):
		if not self.root: return None
		curr = self.root
		while curr.left:
			curr = curr.left
		return curr

	def successor(self, root):
		if not root: return None
		return self.min(root.right)

	def replaceParentChildLink(self, par, child, new_link):
		if not par: return
		if par.left == child:
			par.left = new_link
		else:
			par.right = new_link

	def delete(self, k):
		print "deleting", k, "..."
		curr, par = self.root, None

		while curr and curr.val != k:
			par = curr
			curr = curr.left if k < curr.val else curr.right
		if not curr: return False

		if curr.right:
			r_curr, r_par = curr.right, curr

			# find successor starting from deleted node's right child
			while r_curr.left:
				r_par = r_curr
				r_curr = r_curr.left

			# set successor's left child to deleted node's left child 
			r_curr.left = curr.left

			# save successor's right child since it may be modified to hold deleted node's right child
			r_curr_right = r_curr.right 

			# to avoid pointing successor's right pointer to itself
			if curr.right != r_curr:
				r_curr.right = curr.right

			# replace successor with its right child
			self.replaceParentChildLink(r_par, r_curr, r_curr_right)
			 # replace deleted node with its successor
			self.replaceParentChildLink(par, curr, r_curr)

			# set successor as root if deleted node is root
			if self.root == curr:
				self.root = r_curr
		else: # if deleted node has no successor, use its left child or if no left child, then None, to replace it
			if self.root == curr:
				root = curr.left
			self.replaceParentChildLink(par, curr, curr.left)

		return True
				

bst = BST()
bst.insert(7)
bst.insert(5)
bst.insert(9)
bst.insert(8)
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
print bst.min().val