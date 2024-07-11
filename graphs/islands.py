class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid is None:
            return 0
        rows, cols=len(grid), len(grid[0])
        visit=set()
        island=0


        def bfs(r,c):
            visit.add((r,c))
            q=collections.deque()
            q.append((r,c))
            while q:
                (r,c)=q.popleft()
                directions=[[1,0], [0,1], [-1,0], [0,-1]]
                for dr, dc in directions:
                    if ((r+dr) in range(rows) and (c+dc) in range(cols) and grid[r+dr][c+dc]=="1" and (r+dr,c+dc) not in visit):
                        q.append((r+dr, c+dc))
                        visit.add((r+dr, c+dc))
       
        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visit and grid[r][c]=="1":
                    bfs(r,c)
                    island+=1
        return island