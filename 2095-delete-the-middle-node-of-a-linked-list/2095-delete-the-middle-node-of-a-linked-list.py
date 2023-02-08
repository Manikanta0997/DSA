# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        count = 1
        ptr = head
        ptr2 = head
        while(head.next != None):
            count = count + 1
            head = head.next
        if(count > 1):
            count = count / 2
            for i in range(count-1):
                ptr = ptr.next
            ptr.next = ptr.next.next
            return ptr2
        
            
        
        