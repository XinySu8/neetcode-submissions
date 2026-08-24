class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        fresh = 0
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        ROWS = len(grid)
        COLS = len(grid[0])

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    q.append([i, j])
        
        times = 0
        while fresh > 0 and q:
            for i in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (row in range(ROWS)
                    and col in range(COLS)
                    and grid[row][col] == 1):
                        grid[row][col] = 2
                        q.append([row, col])
                        fresh -= 1
            times += 1
        
        return times if fresh == 0 else -1



