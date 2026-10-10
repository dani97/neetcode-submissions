class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * n for i in range(n)]
        result = []
        cols = set()
        diagPos = set()
        diagNeg = set()
        print(board)

        def dfs(row):
            if row == n:
                copy = ["".join(row) for row in board]
                result.append(copy)
                return
            for col in range(n):
                if col in cols or (row + col) in diagPos or (row-col) in diagNeg:
                    continue
                board[row][col] = 'Q'
                cols.add(col)
                diagPos.add(row+col)
                diagNeg.add(row-col)

                dfs(row + 1)

                board[row][col] = "."
                cols.remove(col)
                diagPos.remove(row+col)
                diagNeg.remove(row-col)
        dfs(0)
        return result
