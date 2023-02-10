# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        li = []
        ptr = head
        if(head != None):
            while(head.next != None):
                li.append(head.val)
                head = head.next
            li.append(head.val)
            head = ptr
            i = 0
            while(head.next != None):
                head.val = li[len(li)-1-i]
                i = i + 1
                head = head.next
            head.val = li[len(li)-i-1]
            return ptr
            
            