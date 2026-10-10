class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        anagram = [0] * 26
        for chars in s:
            anagram[ord(chars) - 97] += 1
        for chars in t:
            anagram[ord(chars) - 97] -= 1
        for val in anagram:
            if val != 0:
                return False
        return True
        