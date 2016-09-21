# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        return self.isSymmetric_(root.left, root.right)
        
    def isSymmetric_(self, left, right):
        if not left or not right:
            return left is None and right is None
        return (left.val == right.val and
                self.isSymmetric_(left.left, right.right) and
                self.isSymmetric_(left.right, right.left))