class Solution:
    def __init__(self):
        self.count = 0
    def climbStairs(self, n: int) -> int:
        self.climb(n)
        return self.count
    def climb(self, n: int):
        if n < 0:
            return
        if n ==0:
            self.count += 1
            return
        self.climb(n-1)
        self.climb(n-2)
        
