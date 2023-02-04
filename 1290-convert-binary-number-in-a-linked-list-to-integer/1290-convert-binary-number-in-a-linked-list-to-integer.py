# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        li = []
        while(head.next != None):
            li.append(head.val)
            head = head.next
        li.append(head.val)
        n = len(li)
        n = n - 1
        num = 0
        for i in range(len(li)):
            num = num + (2 ** n)*li[i]
            n = n - 1
        return num
        