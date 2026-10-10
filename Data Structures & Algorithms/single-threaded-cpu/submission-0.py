class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        result = []
        for idx, task in enumerate(tasks):
            task.append(idx)
        tasks.sort(key=lambda x: x[0])
        time = tasks[0][0]
        index = 0
        heap = []

        while index < len(tasks) or heap:
            while index < len(tasks) and time >= tasks[index][0]:
                heapq.heappush(heap, (tasks[index][1], tasks[index][2]))
                index += 1
            if not heap:
                time = tasks[index][0]
            else:
                t, idx = heapq.heappop(heap)

                result.append(idx)
                time += t
        return result


