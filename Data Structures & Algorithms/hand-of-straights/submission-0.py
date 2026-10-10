class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize != 0:
            return False
        counter = Counter(hand)
        
        minHeap = list(counter.keys())
        heapq.heapify(minHeap)
        while minHeap:
            start = minHeap[0]
            for i in range(start, start+groupSize):
                if i not in counter or counter[i] <= 0:
                    return False
                counter[i] -= 1
                if counter[i] == 0:
                    heapq.heappop(minHeap)

        return True