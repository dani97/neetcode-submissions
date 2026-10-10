class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        hashTable = [0]*26
        trackingHashTable = [0]*26

        for i in s1:
            hashTable[ord(i) - 97] += 1

        for i in range(len(s1)):
            trackingHashTable[ord(s2[i]) - 97] += 1
        
        for i in range(len(s1), len(s2)):
            if hashTable == trackingHashTable:
                return True
            trackingHashTable[ord(s2[i-len(s1)]) - 97] -= 1
            trackingHashTable[ord(s2[i]) - 97] += 1
        return hashTable == trackingHashTable
