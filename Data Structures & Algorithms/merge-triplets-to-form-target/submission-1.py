class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        candidates = []
        for triplet in triplets:
            if triplet == target:
                return True
            for i in range(3):
                if triplet[i] > target[i]:
                    break
            else:
                candidates.append(triplet)
        
        for i in range(3):
            for candidate in candidates:
                if candidate[i] == target[i]:
                    break
            else:
                return False

        return True