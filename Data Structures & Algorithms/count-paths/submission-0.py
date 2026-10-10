from functools import cache

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @cache
        def dfs(i:int, j:int ) -> int:
            if i == m -1:
                return 1
            if j == n-1:
                return 1
            return dfs(i+1, j) + dfs(i, j+1)
        
        return dfs(0,0)