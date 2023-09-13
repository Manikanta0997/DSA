# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        x = head
        while head.next != None:
            count += 1
            head = head.next
        count += 1
        if count > 1:
            head = x
            if n != count:
                for i in range(count - n-1):
                    head = head.next
                head.next = head.next.next
            else:
                x = x.next
            return x
        