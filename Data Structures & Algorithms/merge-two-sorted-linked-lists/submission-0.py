# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        curr1 = list1
        curr2 = list2
        temp = ListNode(-1)
        tail = temp
        while(curr1 is not None and curr2 is not None):
            if (curr1.val <= curr2.val):
                tail.next = curr1
                curr1 = curr1.next
            else: 
                tail.next = curr2
                curr2 = curr2.next
            tail = tail.next

        if curr1 is not None:
            tail.next = curr1
        else:
            tail.next = curr2
    
        return temp.next

