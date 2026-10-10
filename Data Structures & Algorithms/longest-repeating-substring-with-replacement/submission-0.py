class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length = 0
        hmap = {}
        l = 0
        for i in range(len(s)):
            if s[i] in hmap:
                hmap[s[i]] += 1
            else:
                hmap[s[i]] = 1
            values = hmap.values()
            max_value = max(values)
            length = sum(values)
            if length - max_value > k:
                hmap[s[l]] -= 1
                if hmap[s[l]] == 0:
                    del hmap[s[l]]
                l += 1
            max_length = max(max_length, i - l + 1)
        
        return max_length