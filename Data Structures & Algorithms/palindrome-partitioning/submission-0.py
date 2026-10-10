class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i, j = i+1, j-1
            return True
        
        result = []
        partition = []
        
        def dfs(i):
            if i >= len(s):
                result.append(partition.copy())
                return
            
            for j in range(i, len(s)):
                if isPalindrome(i,j):
                    partition.append(s[i:j+1])
                    dfs(j+1)
                    partition.pop()
        dfs(0)
        return result