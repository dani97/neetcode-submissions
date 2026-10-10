class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        heap = []
        N = len(profits)
        projects = [(capital[i], profits[i]) for i in range(N)]
        projects.sort()

        index = 0

        for i in range(k):
            while index < N and projects[index][0] <= w:
                heapq.heappush(heap, -projects[index][1])
                index += 1
            if not heap:
                break
            w += -heapq.heappop(heap)
        return w