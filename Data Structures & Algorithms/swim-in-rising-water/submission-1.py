class Node:
    def __init__(self, pos: (int, int), val: int):
        self.pos = pos
        self.val = val
    
    def __repr__(self):
        return f"val: {self.val} pos: {self.pos}"
    
    def __lt__(self, other):
        return self.val < other.val
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        directions = [(0,1), (1,0), (-1, 0), (0, -1)]
        min_time = 0
        size = len(grid)
        visited = set()
        heap = [Node((0, 0), grid[0][0])]
        heapq.heapify(heap)
        while heap:
            node = heapq.heappop(heap)
            min_time = max(min_time, node.val)
            if node.pos[0] == size - 1 and node.pos[1] == size - 1:
                break
            for dr in directions:
                nrow = node.pos[0] + dr[0]
                ncol = node.pos[1] + dr[1]

                if nrow < 0 or ncol < 0 or nrow >= size or ncol >= size or (nrow, ncol) in visited:
                    continue
                heapq.heappush(heap, Node((nrow, ncol), grid[nrow][ncol]))
                visited.add((nrow, ncol))
        return min_time
            
            

