class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        ROW, COL = len(grid), len(grid[0])
        directions = [[1,0], [-1, 0], [0, 1], [0, -1]]
        maxArea = 0

        def bfs(r,c):
            area = 1
            grid[r][c] = 0
            q = deque()
            q.append((r,c))
            while q:
                qr, qc = q.popleft()
                for nr, nc in directions:
                    row = qr + nr
                    col = qc + nc
                    if (row < 0 or col < 0 or
                    row >= ROW or col >= COL or
                    grid[row][col] == 0):
                        continue
                    q.append((row, col))
                    grid[row][col] = 0
                    area += 1
            return area
                        

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    curArea = bfs(r,c)
                    maxArea = max(maxArea, curArea)
        
        return maxArea
                    
