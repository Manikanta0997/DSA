# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        str1 = ""
        str2 = ""
        ptr = l1
        ptr1 = l1
        ptr2 = l1
        while(l1.next != None):
            str1 = str1 + str(l1.val)
            l1 = l1.next
        str1 = str1 + str(l1.val)
        while(l2.next != None):
            str2 = str2 + str(l2.val)
            l2 = l2.next
        str2 = str2 + str(l2.val)
        str1 = int(str1)
        str2 = int(str2)
        str1 = str(str1 + str2)
        count = 0
        ptr.val = int(str1[0:1])
        for i in range(1,len(str1)):
            if(ptr.next == None):
                ptr.next = ListNode(int(str1[i:i+1]))
                ptr = ptr.next
            else:
                ptr = ptr.next
                ptr.val = str1[i:i+1]
        ptr.next = None
        return ptr1
        
            
        
        