



# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution(object):
    
    
    def createLinkedList(self, lst):
        dummy = ListNode()
        current = dummy
        for value in lst:
            current.next = ListNode(value)
            current = current.next
        return dummy.next
    
    def mergeTwoLists(self, list1, list2):

        dummy = ListNode()
        current = dummy

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
            
            
        if list1:
            current.next = list1
        elif list2:
            current.next = list2
            
        return dummy.next
        

        
s = Solution()

list1 = s.createLinkedList([1,2,4])
list2 = s.createLinkedList([1,3,4])
print(s.mergeTwoLists(list1, list2))

        