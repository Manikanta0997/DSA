# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeNodes(self, head):
        ptr = head
        ptr2 = head
        head = head.next
        t = 1
        add = 0
        count = 0
        while(t == 1):
            if(head.val == 0):
                ptr.val = add
                ptr = ptr.next
                count = count + 1
                add = 0
                if(head.next == None):
                    t = 0
            else:
                add = add + head.val
            head = head.next
        ptr = ptr2
        print(count)
        for i in range(count-1):
            ptr = ptr.next
        ptr.next = None
        return ptr2
                
        