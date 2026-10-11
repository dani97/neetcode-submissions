class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        agm_map = {}
        for word in strs:
            c_map = [0]*26
            for letter in word:
                c_map[ord(letter) - 97] += 1
            #print(c_map)
            key = ",".join(map(str,c_map))
            #print(key)
            if key in agm_map:
                agm_map[key].append(word)
            else:
                agm_map[key] = [word]

        result = []
        for value in agm_map.values():
            result.append(value)
        return result