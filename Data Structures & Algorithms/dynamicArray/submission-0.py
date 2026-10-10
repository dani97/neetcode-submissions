class DynamicArray:
    
    def __init__(self, capacity: int):
        self.array = [0]*capacity
        self.capacity = capacity
        self.size = 0

    def get(self, i: int) -> int:
        if i >= self.size:
            raise Exception('Array out of bounds')
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        if i >= self.size:
            raise Exception('Array out of bounds')
        self.array[i] = n

    def pushback(self, n: int) -> None:
        if self.size >= self.capacity:
            self.resize()
        self.array[self.size] = n
        self.size += 1

    def popback(self) -> int:
        self.size -= 1
        return self.array[self.size]
 

    def resize(self) -> None:
        self.capacity *= 2
        tmp_array = [0]*self.capacity
        for i in range(self.size):
            tmp_array[i] = self.array[i]
        self.array = tmp_array

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity
