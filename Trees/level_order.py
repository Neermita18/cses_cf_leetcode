# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def dfs(root):
            if root is None:
                return -1
            l=dfs(root.left)
            r=dfs(root.right)
            return 1+max(l,r)

        def level(root, height,r):
            if root is None:
                return 0
            if height==0:
                r.append(root.val)
            elif height>0:
                level(root.left, height-1,r)
                level(root.right, height-1,r)

        def store(root):
            result=[]
            h= dfs(root)
            for i in range(h+1):
                l=[]
                level(root,i,l)
                result.append(l)
            return result
        result=store(root)
        print(result)
        return result