class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_symbols = {'(': ')', '{': '}', '[': ']'}
        for symbol in s:
            if symbol in open_symbols:
                stack.append(symbol)
            else:
                if not stack: return False
                val =  stack.pop()
                if open_symbols[val] != symbol:
                    return False
        return len(stack) == 0
        