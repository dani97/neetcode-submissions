class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        if a != 0:
            heap.append((-a, 'a'))
        if b != 0:
            heap.append((-b, 'b'))
        if c != 0:
            heap.append((-c, 'c'))
        heapq.heapify(heap)
        result = []

        while heap:
            freq, ch = heapq.heappop(heap)
            if len(result) < 2:
                result.append(ch)
                if freq < -1:
                    heapq.heappush(heap, (freq + 1, ch))
            elif result[-2] == ch and result[-1] == ch:
                if heap:
                    freq2, ch2 = heapq.heappop(heap)
                    result.append(ch2)
                    if freq2 < -1:
                        heapq.heappush(heap, (freq2 + 1, ch2))
                    heapq.heappush(heap, (freq, ch))
                else:
                    break
            else:
                result.append(ch)
                if freq < -1:
                    heapq.heappush(heap, (freq + 1, ch))
        return "".join(result)