# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        str1 = ""
        ptr = l1
        ret = l1
        str2 = ""
        while(l1.next != None):
            str1 = str1 + str(l1.val)
            l1 = l1.next
        str1 = str1 + str(l1.val)
        while(l2.next != None):
            str2 = str2 + str(l2.val)
            l2 = l2.next
        str2 = str2 + str(l2.val)
        str1 = str1[::-1]
        str2 = str2[::-1]
        add = str(int(str1) + int(str2))
        add = int(add)
        li = []
        while(add > 0):
            li.append(add%10)
            add = add / 10
        print(li)
        print(ptr.val)
        count = 0
        for i in range(len(li)):
            if(ptr.next == None):
                if(count == 0):
                    ptr.val = li[i]
                    count = count + 1
                else:
                    newnode = ListNode(li[i])
                    ptr.next = newnode
                    ptr = newnode
            else:
                ptr.val = li[i]
                ptr = ptr.next
        return ret
        
                
            
        
            
            
            