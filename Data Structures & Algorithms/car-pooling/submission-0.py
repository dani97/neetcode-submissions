class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        intervals = []

        for count, start, end, in trips:
            intervals.append([start, count])
            intervals.append([end, -count])
        
        intervals.sort()

        passengers = 0
        curPass = 0
        for _, passengers in intervals:
            curPass += passengers
            if curPass > capacity:
                return False
        
        return True

        