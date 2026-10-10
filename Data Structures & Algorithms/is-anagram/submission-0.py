class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anagram = [0] * 26
        for chars in s:
            anagram[ord(chars) - 97] += 1
        for chars in t:
            anagram[ord(chars) - 97] -= 1
        return len(set(anagram)) ==1 and anagram[0] == 0
        