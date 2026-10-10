class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m = len(grid)
        n = len(grid[0])
        queue = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    queue.append((i,j))
        depth = 0
        directions = [(0,1), (0,-1),(1,0), (-1,0)]
        while queue:
            count = len(queue)
            for _ in range(count):
                i,j = queue.popleft()
                grid[i][j] = min(grid[i][j], depth)
                for dr in directions:
                    nr = i + dr[0]
                    nc = j + dr[1]
                    if nr <0 or nr >= m or nc < 0 or nc >= n or grid[nr][nc]!= 2147483647:
                        continue
                    queue.append((nr, nc))
            depth += 1
        
                        
        