class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROW, COL = len(matrix), len(matrix[0])

        bot, top = 0, ROW-1
        while bot <= top:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                bot = row + 1
            elif target < matrix[row][0]:
                top = row - 1
            else:
                break
        if not (bot <= top):
            return False
        left, right = 0, COL-1
        while left <= right:
            col = (left + right) // 2
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                left = col + 1
            elif matrix[row][col] > target:
                right = col - 1
        return False
