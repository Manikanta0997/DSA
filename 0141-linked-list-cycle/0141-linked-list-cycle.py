# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        li = []
        if head != None:
            while head.next != None:
                if head in li:
                    return True
                else:
                    li.append(head)
                head = head.next
        