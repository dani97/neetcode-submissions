class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        hs = set()
        def dfs(word, i ,j):
            if len(word) == 0:
                return True
            if i < 0 or i >= m or j < 0 or j >= n:
                return False
            if board[i][j] != word[0]:
                return False
            if (i, j) in hs:
                return False
            hs.add((i,j))
            down = dfs(word[1:], i+1, j)
            right = dfs(word[1:], i, j + 1)
            up = dfs(word[1:], i -1, j)
            left = dfs(word[1:], i , j-1)
            hs.remove((i, j))
            return down or right or up or left
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(word, i, j):
                        return True
        return False