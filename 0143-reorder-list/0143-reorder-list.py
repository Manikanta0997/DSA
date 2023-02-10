# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        li = []
        ptr = head
        while(head.next != None):
            li.append(head.val)
            head = head.next
        li.append(head.val)
        head = ptr
        count = 0
        for i in range(len(li) / 2):
            newnode = ListNode(li[len(li)-1-count])
            count = count + 1
            x = head.next
            head.next = newnode
            newnode.next = x
            y = newnode
            head = head.next.next
        if(len(li)%2 == 0):
            y.next = None
        else:
            head.next = None
        return ptr