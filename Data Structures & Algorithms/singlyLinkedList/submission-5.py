class Node:
    def __init__(self, val: int):
        self.next = None
        self.val = val

class LinkedList:  
    def __init__(self):
        self.head = Node(-1) # sentinel node
        self.tail = None
    
    def get(self, index: int) -> int:
        cursor = self.head.next
        k = 0
        while cursor != None:
            if k == index:
                return cursor.val
            cursor = cursor.next
            k += 1
        return -1

    def insertHead(self, val: int) -> None:
        node = Node(val)
        node.next = self.head.next
        self.head.next = node
        if not self.tail:
            self.tail = node
        print(self.getValues())
        

    def insertTail(self, val: int) -> None:
        node = Node(val)
        if self.tail:
            self.tail.next = node
            self.tail = node
        else:
            self.head.next = node
            self.tail = node
        print(self.getValues())

    def remove(self, index: int) -> bool:
        k = 0
        cursor = self.head
        while k < index and cursor:
            print(cursor.val)
            k += 1
            cursor = cursor.next
            
            

        if cursor and cursor.next:
            if cursor.next == self.tail:
                self.tail = cursor
            cursor.next = cursor.next.next
            return True
        return False
   
    def getValues(self) -> List[int]:
        cursor = self.head.next
        output = []
        while cursor:
            output.append(cursor.val)
            cursor = cursor.next
        return output

