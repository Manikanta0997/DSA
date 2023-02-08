# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        count = 1
        ptr = head
        while(head.next != None):
            head = head.next
            count = count + 1
        count = count / 2
        for i in range(count):
            ptr = ptr.next
        return ptr
        