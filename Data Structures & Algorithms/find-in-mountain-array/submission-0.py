class Solution:

    def __init__(self):
        self.cache = {}

    def getFromMountainArray(self, mountainArr: 'MountainArray', idx: int) -> int:
        if idx not in self.cache:
            self.cache[idx] = mountainArr.get(idx)
        return self.cache[idx]

    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        peak_next = self.findPeak(mountainArr)
        print("peak", peak_next)
        left = 0
        right = peak_next - 1

        if target >= self.getFromMountainArray(mountainArr, 0) and target <= self.getFromMountainArray(mountainArr, right):
            while left <= right:
                mid = (left + right) // 2

                mid_val = self.getFromMountainArray(mountainArr, mid)
                if mid_val == target:
                    return mid
                elif mid_val > target:
                    right = mid - 1
                else:
                    left = mid + 1

        left = peak_next
        right = mountainArr.length() - 1

        while left <= right:
            mid = (left + right) // 2
            mid_val = self.getFromMountainArray(mountainArr, mid)
            if mid_val == target:
                return mid
            elif mid_val < target:
                right = mid - 1
            else:
                left = mid + 1
        return -1

    def findPeak(self, mountainArr: 'MountainArray') -> int:
        left = 1
        right = mountainArr.length() - 2
        while left <= right:
            mid = (left + right) // 2

            if self.getFromMountainArray(mountainArr, mid - 1) >= self.getFromMountainArray(mountainArr, mid):
                right = mid - 1
            else:
                left = mid + 1
        
        return left