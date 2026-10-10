from functools import cache
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        @cache
        def dfs(i, j, pos) -> bool:
            if pos == len(s3):
                return i == len(s1) and j == len(s2)
            res = False
            if i < len(s1) and s1[i] == s3[pos]:
                res = dfs(i+1, j, pos+1)
            if j < len(s2) and s2[j] == s3[pos]:
                res = res or dfs(i, j+1, pos+1)
            return res
        return dfs(0,0,0)


        