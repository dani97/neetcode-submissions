class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        
        hash_strings = {}
        for string in strs:
            hash_table = [0]*26
            for char in string:
                hash_table[ord(char) - 97] += 1
            key = ','.join(map(str,hash_table))
            print(key)
            if key in hash_strings:
                hash_strings[key].append(string)
            else:
                hash_strings[key] = [string]
        return hash_strings.values()


