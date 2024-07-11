class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
  
        if grid is None:
            return 0
        rows, cols= len(grid), len(grid[0])
        islands=[]
        visit=set()
        max_area = 0

        def bfs(r,c):
            area = 1
            visit.add((r,c))
            q=collections.deque()
            q.append((r,c))
            while q:
                (r,c)=q.popleft()
                directions=[[1,0], [0,1],[-1,0],[0,-1]]
                for dr, dc in directions:
                    if (r+dr in range(rows) and c+dc in range(cols) and (r+dr, c+dc) not in visit and grid[r+dr][c+dc]==1):
                        visit.add((r+dr,c+dc))
                        q.append((r+dr, c+dc))
                        area += 1
            
            return area
            
                         
        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visit and grid[r][c]==1:
                    max_area = max(max_area, bfs(r, c))
        print(max_area)
        return max_area