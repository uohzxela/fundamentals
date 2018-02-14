# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import namedtuple

Result = namedtuple('Result', ('diameter', 'height'))

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.helper(root).diameter
    
    def helper(self, root):
        if not root:
            return Result(0, 0)

        left = self.helper(root.left)
        right = self.helper(root.right)
        
        diameter = max(left.height + right.height, left.diameter, right.diameter)
        height = max(left.height, right.height) + 1
        
        return Result(diameter, height)
