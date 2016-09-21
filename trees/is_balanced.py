# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getHeight(self, root):
        if root == None: 
            return 0
        left = self.getHeight(root.left) 
        right = self.getHeight(root.right)
        if left != None and right != None and abs(left - right) <= 1:  
            return max(left,right) + 1

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.getHeight(root) != None
