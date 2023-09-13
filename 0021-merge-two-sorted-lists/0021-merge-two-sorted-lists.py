# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        ans = head
        if list1 or list2:
            while list1 and list2:
                if list1.val < list2.val:
                    head.val = list1.val
                    head.next = ListNode()
                    head = head.next
                    list1 = list1.next
                else:
                    head.val = list2.val
                    head.next = ListNode()
                    head = head.next
                    list2 = list2.next
            if list1 != None:
                while list1.next != None:
                    head.val = list1.val
                    head.next = ListNode()
                    head = head.next
                    list1 = list1.next
                head.val = list1.val
            elif list2 != None:
                while list2.next != None:
                    head.val = list2.val
                    head.next = ListNode()
                    head = head.next
                    list2 = list2.next
                head.val = list2.val
            return ans

        