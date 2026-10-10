class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m = len(board)
        n = len(board[0])
        queue = deque()
        directions = [(1,0), (-1, 0), (0, 1), (0, -1)]
        def bfs(pos):
            queue = deque()
            visited = set()
            queue.append(pos)
            visited.add((i,j))
            while queue:
                count = len(queue)
                for _ in range(count):
                    x, y = queue.popleft()
                    for dr in directions:
                        nrow = x + dr[0]
                        ncol = y + dr[1]

                        if nrow <0 or ncol < 0 or nrow == m or ncol == n:
                            return
                        if (nrow, ncol) not in visited and board[nrow][ncol] == 'O':
                            queue.append((nrow, ncol))
                            visited.add((nrow, ncol))
            for cell in visited:
                board[cell[0]][cell[1]] = 'X'

                        


        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    bfs((i,j))
