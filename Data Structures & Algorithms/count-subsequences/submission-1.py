from functools import cache
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)
        @cache
        def dfs(i, j):
            if j == n:
                return 1
            if i == m:
                return 0
            if m - i < n - j:
                return 0
            res = 0
            if s[i] == t[j]:
                res += dfs(i+1, j+1)
            res += dfs(i+1, j)
            return res
        return dfs(0,0)