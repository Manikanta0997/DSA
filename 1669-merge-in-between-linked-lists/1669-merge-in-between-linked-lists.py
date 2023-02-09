class Solution(object):
    def mergeInBetween(self, list1, a, b, list2):
        ptr = list1
        ptr2 = list1.next
        count = 1
        while(count != a):
            ptr2 = ptr2.next
            list1 = list1.next
            count = count + 1
        ptr3 = list1.next
        list1.next = list2
        while(list1.next != None):
            list1 = list1.next
        while(count != b):
            ptr3 = ptr3.next
            count = count + 1
        list1.next = ptr3.next
        return ptr
                