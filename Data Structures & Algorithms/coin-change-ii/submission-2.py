class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        memo = {}

        def dfs(i, amount) -> int:
            if amount == 0:
                return 1
            if i >= len(coins):
                return 0
            if (i, amount) in memo:
                return memo[(i, amount)] 
            res = 0
            if amount >= coins[i]:
                res = dfs(i+ 1, amount)
                res += dfs(i, amount - coins[i])
            memo[(i, amount)] = res
            return res
            
            
        return dfs(0, amount)