# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        ptr1 = head
        length = 0
        re = 0
        while(head.next!=None):
            head = head.next
            length = length + 1
        length = length + 1
        length = length / 2
        head = ptr1
        li = []
        for i in range(length):
            li.append(head.val)
            head = head.next
        for i in range(length):
            x = li[length-i-1]
            if(x + head.val > re):
                re = x + head.val
            head = head.next
        return re
        