class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []
        length = len(nums)
        def createPermutations(current):
            if len(current) == length:
                output.append(list(current.keys()))
                return
            for i in nums:
                if len(current) != 0 and i in current:
                    continue
                current[i] = 1
                createPermutations(current)
                del current[i]
        createPermutations({})
        return output
