class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)

        heap = [(-freq, ch) for ch, freq in counter.items()]

        heapq.heapify(heap)
        result = []

        while heap:
            freq, ch = heapq.heappop(heap)
            if not result:
                result.append(ch)
                if freq < -1:
                    heapq.heappush(heap, (freq + 1, ch))
            elif result[-1] != ch:
                result.append(ch)
                if freq < -1:
                    heapq.heappush(heap, (freq + 1, ch))
            else:
                if heap:
                    freq2, ch2 = heapq.heappop(heap)
                    result.append(ch2)
                    if freq2 < -1:
                        heapq.heappush(heap, (freq2 + 1, ch2))
                    heapq.heappush(heap, (freq, ch))
                else:
                    return ""
        return "".join(result)
        