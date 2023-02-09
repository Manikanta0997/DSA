# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        li = []
        ptr = head
        ptr2 = head
        if(head!=None):
            while(head.next!= None):
                li.append(head.val)
                head = head.next
            li.append(head.val)
            li.sort()
            for i in range(len(li)):
                ptr.val = li[i]
                ptr = ptr.next
            return ptr2
        
        