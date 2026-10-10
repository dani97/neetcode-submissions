class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        maps = {}
        for index in range(len(nums)):
            diff = target - nums[index]
            if diff not in maps:
                maps[nums[index]] = index
            else:
                return [maps[target - nums[index]], index]
        return [0,1]