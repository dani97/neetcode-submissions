class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map1 = [0]*26
        ascii_a = ord('a')
        for c in s:
            map1[ord(c) - ascii_a] += 1

        for c in t:
            map1[ord(c) - ascii_a] -= 1
        
        for count in map1:
            if count != 0:
                return False
        return True
