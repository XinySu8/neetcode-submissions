class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])
        q = deque()
        pac = [[False] * COLS for _ in range(ROWS)]
        atl = [[False] * COLS for _ in range(ROWS)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]


        # bfs
        def bfs(source, ocean):
            q = deque(source)

            for r, c in source:
                ocean[r][c] = True
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if(0 <= nr < ROWS and 0 <= nc <COLS and
                        not ocean[nr][nc] and
                        heights[nr][nc] >= heights[r][c]):
                            ocean[nr][nc] = True
                            q.append((nr, nc))

        pacific = []
        atlantic = []
        # (r == 0 or c == 0) and (r == ROWS - 1 or c == COLS - 1)
        for i in range(ROWS):
            pacific.append([i, 0])
            atlantic.append([i, COLS - 1])
        for j in range(COLS):
            pacific.append([0, j])
            atlantic.append([ROWS - 1, j])

            

        bfs(pacific, pac)
        bfs(atlantic, atl)

        res = []

        for r in range(ROWS):
            for c in range(COLS):
                if pac[r][c] and atl[r][c]:
                    res.append([r, c])
        return res

