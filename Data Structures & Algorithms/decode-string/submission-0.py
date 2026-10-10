class Solution:
    def decodeString(self, s: str) -> str:
        count_stack = deque()
        s_stack = deque()

        current = ""
        k = 0

        for c in s:
            if c.isdigit():
                k = k * 10 + int(c)
            elif c == "[":
                count_stack.append(k)
                s_stack.append(current)
                current = ""
                k = 0
            elif c == "]":
                temp = current
                freq = count_stack.pop()
                current = s_stack.pop()
                current += freq * temp
            else:
                current += c
        
        return current