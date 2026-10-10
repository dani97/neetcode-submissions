class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}

        for idx, c in enumerate(s):
            lastIndex[c] = idx
        
        res = []
        size = end = 0
        for idx, c in enumerate(s):
            size += 1
            end = max(end, lastIndex[c])

            if end == idx:
                res.append(size)
                size = 0
        
        return res