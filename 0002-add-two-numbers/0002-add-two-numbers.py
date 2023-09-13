# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        str1 = ''
        str2 = ''
        while l1:
            str1 = str(l1.val) + str1 
            l1 = l1.next
        while l2:
            str2 = str(l2.val) + str2
            l2 = l2.next
        res = str(int(str1) + int(str2))[::-1]
        head = ListNode()
        x = head
        for i in range(len(res)):
            head.val = int(res[i:i+1])
            if i != len(res) - 1: 
                head.next = ListNode()
                head = head.next
        return x
            
            
        