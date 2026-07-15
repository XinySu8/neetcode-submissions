class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        l = len(word)
        path = set()
        
        def dfs(i, j, k):
            if k == l:
                return True
            if (i < 0 or j < 0 or i >= rows or j >= cols or
                (i, j) in path or word[k] != board[i][j]):
                return False

            path.add((i, j))
            res = (dfs(i + 1, j, k + 1) or
            dfs(i, j + 1, k + 1) or
            dfs(i - 1, j, k + 1) or
            dfs(i, j - 1, k + 1)
            )
            path.remove((i, j))
            return res
        
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False
        