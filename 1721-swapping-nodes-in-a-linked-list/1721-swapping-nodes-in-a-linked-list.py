# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        ptr = head
        ptr3 = head
        count = 0
        while(head.next != None):
            count = count + 1
            head = head.next
        head = ptr
        for i in range(k-1):
            head = head.next
        count = count + 1
        count = count - k
        for i in range(count):
            ptr = ptr.next
        x = head.val
        head.val = ptr.val
        ptr.val = x
        return ptr3
        
            
        