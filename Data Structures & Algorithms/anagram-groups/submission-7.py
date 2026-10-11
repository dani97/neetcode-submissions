class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        agm_map = {}
        for word in strs:
            c_map = [0]*26
            for letter in word:
                c_map[ord(letter) - 97] += 1
            key = tuple(c_map)
            if key in agm_map:
                agm_map[key].append(word)
            else:
                agm_map[key] = [word]

        return list(agm_map.values())