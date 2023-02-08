# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        count = 0
        ptr = node
        while(node.next != None):
            node.val = node.next.val
            node = node.next
            count = count + 1
        for i in range(count-1):
            ptr = ptr.next
        
        ptr.next = None          
