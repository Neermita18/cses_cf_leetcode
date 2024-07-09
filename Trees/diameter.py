# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.d=0
        def dfs(root):
            if root is None:
                return -1
            l=dfs(root.left)
            r=dfs(root.right)
            h= 1+max(l,r)
            self.d= max(self.d,(l+r+2))
            return h
        dfs(root)
        return self.d
        