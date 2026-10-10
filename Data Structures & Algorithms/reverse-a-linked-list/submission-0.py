# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: # 0 or 1 node
            return head
        sentinel  = ListNode(-1)
        cursor = head
        while cursor:
            temp = cursor.next
            cursor.next = sentinel.next
            sentinel.next = cursor
            cursor = temp
        return sentinel.next
        