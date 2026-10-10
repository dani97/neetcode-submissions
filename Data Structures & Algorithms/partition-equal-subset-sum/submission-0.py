class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total%2 != 0:
            return False
        
        target = total // 2

        def backtrack(pos:int, target: int) -> bool:
            if pos >= len(nums) or target < 0:
                return False
            if target == 0:
                return True
            
            return backtrack(pos + 1, target) or backtrack(pos + 1, target - nums[pos])
        
        return backtrack(0, target)
            
    
