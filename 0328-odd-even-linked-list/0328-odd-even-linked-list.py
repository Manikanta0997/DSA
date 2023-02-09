# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        ptr = head
        ptr2 = head
        count = 0
        if(head != None):
            while(head.next != None):
                head = head.next
                count = count + 1
            count = count + 1
            for i in range(count/2):
                newnode = ListNode(ptr.next.val)
                head.next = newnode
                head = newnode
                ptr.next = ptr.next.next
                ptr = ptr.next
            return ptr2

                
        