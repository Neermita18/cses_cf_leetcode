# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        def dfs(node, maxv):
            if not node:
                return
            if node.val >= maxv:
                self.res += 1
            maxv = max(maxv, node.val)
            dfs(node.left, maxv)
            dfs(node.right, maxv)
        
        dfs(root, root.val)
        return self.res
        