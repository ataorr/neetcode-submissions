class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        result = 0
        directions = [[1,0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        def bfs(r,c):
            q = deque()
            grid[r][c] = "0"
            q.append((r,c))
            while q:
                row, col = q.popleft()
                for nr, nc in directions:
                    nextRow = row + nr
                    nextCol = col + nc
                    if (nextRow >= 0 and nextCol >= 0
                        and nextRow < ROWS and nextCol < COLS
                        and grid[nextRow][nextCol] == "1"):
                        grid[nextRow][nextCol] = 0
                        q.append((nextRow, nextCol))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    bfs(r,c)
                    result += 1
        return result

