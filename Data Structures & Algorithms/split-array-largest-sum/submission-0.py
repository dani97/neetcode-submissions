class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def canSplitIntok(cap: int) -> bool:
            part_total = 0
            count = 0

            for num in nums:
                if part_total + num <= cap:
                    part_total += num
                else:
                    part_total = num
                    count += 1
                    if count == k:
                        return False
            return True

        left, right = max(nums), sum(nums)

        while left <= right:
            mid = left + (right - left) // 2
            if canSplitIntok(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left
