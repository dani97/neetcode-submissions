class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        stack = deque()
        res = deque()

        for i in range(len(heights) - 1, -1, -1):
            while stack and heights[i] > stack[-1]:
                stack.pop()
            if not stack:
                res.appendleft(i)
            stack.append(heights[i])
        return list(res)