class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        ht = Counter(nums)
        freq = [[] for _ in range(len(nums) + 1)]
        for i in ht.keys():
            freq[ht[i]].append(i)
        res = []
        for i in range(len(nums), 0, -1):
            res += freq[i]
        return res[:k]

        


        