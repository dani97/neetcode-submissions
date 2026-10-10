from functools import cache
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        last = len(nums) - 1 
        
        @cache
        def dfs(i: int, target):
            if i == last:
                if nums[i] == target ==0:
                    return 2
                return 1 if nums[i] == abs(target) else 0   
            return dfs(i+1, target - nums[i]) + dfs(i+1, target + nums[i])

        return dfs(0, target)