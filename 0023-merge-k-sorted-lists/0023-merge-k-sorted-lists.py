# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        li = []
        for i in range(len(lists)):
            while lists[i]:
                li.append(lists[i].val)
                lists[i] = lists[i].next
        li.sort()
        if li:
            head = ListNode()
            x = head
            for i in range(len(li)):
                head.val = li[i]
                if i + 1 != len(li):
                    head.next = ListNode()
                    head = head.next
            return x
            