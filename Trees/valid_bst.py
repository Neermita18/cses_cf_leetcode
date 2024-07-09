# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    import heapq
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        x=[]
        def inorder(root):
            if root is None:
                return
            inorder(root.left)
            x.append(root.val)
            inorder(root.right)
        inorder(root)

        for i in range(1, len(x)):
            if x[i-1] >= x[i]:
                return False
        return True