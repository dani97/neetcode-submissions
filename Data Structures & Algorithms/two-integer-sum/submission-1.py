class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map1 = {}
        for index, num in enumerate(nums):
            if target - num in map1:
                return [map1[target - num], index]
            map1[num] = index
        return [0,1]
