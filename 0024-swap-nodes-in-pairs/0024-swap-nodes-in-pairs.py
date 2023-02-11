# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        ptr = head
        count = 0
        if(head != None):
            while(head.next != None):
                count = count + 1
                head = head.next
            count = count + 1
            head = ptr
            for i in range(count / 2):
                x = head.val
                head.val = head.next.val
                head.next.val = x
                head = head.next.next
            return ptr
            
        
        