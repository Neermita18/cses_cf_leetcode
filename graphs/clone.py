"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visit={}
        def dfs(node):
            if node is None:
                return 
            if node in visit:
                return visit[node]
            c=Node(node.val)
            visit[node]=c
            for x in node.neighbors:
                c.neighbors.append(dfs(x))
            return c
        return dfs(node)