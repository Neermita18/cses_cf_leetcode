class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
  
        if grid is None:
            return 0
        rows, cols= len(grid), len(grid[0])
        visit=set()
        def dfs(r,c):
            if r not in range(rows) or c not in range(cols) or (r,c) in visit or grid[r][c]!=1:
                return 0
            visit.add((r,c))
            return (1+ dfs(r+1,c)+
            dfs(r,c+1)+
            dfs(r-1,c)+
            dfs(r,c-1))
        area=0
        for r in range(rows):
            for c in range(cols):
                area=max(dfs(r,c),area)
        return area