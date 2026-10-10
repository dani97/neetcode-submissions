class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        length = len(s)
        flags = [False] * (length + 1)
        flags[-1] = True
        
        
        for i in range(length, -1, -1):
            for word in wordDict:
                if i + len(word) <= length and s[i:i+len(word)] == word:
                    flags[i] = flags[i + len(word)]
                if flags[i]:
                    break
        return flags[0]
                    