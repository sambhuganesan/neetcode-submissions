# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 1
        curr1 = head
        curr = head
        length = 0

        while (curr1 != None):
            curr1 = curr1.next
            length += 1
        fromFront = (length+1) -n
        if (length == 1):
            curr1 = None
            return curr1
        if (fromFront == 1):
            return curr.next
        while (curr != None):
            if (fromFront == length and count == fromFront-1):
                curr.next = None
            elif (count == fromFront-1 and count != length):
                curr.next = curr.next.next
            curr = curr.next
            count += 1
        return head