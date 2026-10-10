class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        
        if not self.minstack or val < self.getMin():
            self.minstack.append(len(self.stack) - 1) # append index
        print(self.stack, self.minstack)


    def pop(self) -> None:
        val = self.stack.pop()
        min_stack_top = self.minstack[-1]
        if min_stack_top >= len(self.stack):
            self.minstack.pop()
        print(self.stack, self.minstack)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack[self.minstack[-1]]
        
