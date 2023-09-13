# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        count = 0
        x = head
        while head.next != None:
            count += 1
            head = head.next
        count += 1
        if count % 2 == 0:
            count = int(count / 2)
        else:
            count = int(count / 2) + 1
        head = x
        for i in range(count):
            if i + 1 == count:
                temp = head.next
                head.next = None
            head = head.next
        head = x
        prev, curr = None, temp
        while curr != None:
            temp1 = curr.next
            curr.next = prev
            prev = curr
            curr = temp1
        count = 0
        while prev != None:
            tmp1, tmp2 = head.next, prev.next
            head.next = prev
            prev.next = tmp1
            head, prev = tmp1, tmp2
        return x
            
                
            
            
            
        
                