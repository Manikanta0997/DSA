# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        count = 0
        ptr = head
        while(head.next != None):
            count = count + 1
            head = head.next
        if(count >= 1):
            count = count - n 
            head = ptr
            if(count >=0):
                for i in range(count):
                    head = head.next
                head.next = head.next.next
            else:
                ptr = ptr.next
            return ptr

            
        