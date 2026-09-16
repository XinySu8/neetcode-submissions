class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])
        visit = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            visit.add((r, c))
            group = set()
            surround = True

            while q:
                r, c = q.popleft()
                group.add((r, c))
                for nr, nc in directions:
                    if ((r + nr, c + nc) not in visit and 
                        r + nr < ROWS and c + nc < COLS and
                        r + nr >= 0 and c + nc >= 0 and
                        board[r + nr][c + nc] == "O"
                        ):
                            q.append((r + nr, c + nc))
                            visit.add((r + nr, c + nc))
                    if r == 0 or r == ROWS-1 or c == 0 or c == COLS - 1:
                        surround = False
            
            if surround:
                for r, c in group:
                    board[r][c] = "X"
            

        for i in range(1, ROWS - 1):
            for j in range(1, COLS - 1):
                if  board[i][j] == "O" and (i, j) not in visit:
                    bfs(i, j)

                        
        