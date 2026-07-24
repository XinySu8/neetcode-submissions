class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visit = set()
        maxland = 0

        def bfs(i, j):
            area = 1
            q = collections.deque()
            q.append((i, j))
            visit.add((i, j))
            
            while q:
                directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
                row, col = q.popleft()
                for dr, dc in directions:
                    r = row + dr
                    c = col + dc
                    if (r in range(rows) and
                        c in range(cols) and
                        grid[r][c] == 1 and
                        (r, c) not in visit):
                        area += 1
                        q.append((r, c))
                        visit.add((r, c))
            return area

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i, j) not in visit:
                    maxland = max(maxland, bfs(i, j))

        return maxland