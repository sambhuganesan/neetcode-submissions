# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # you can create a adjacency matrix and solve the problem that way
        # space would be O(n^2) though.

        # for o(1) space just use two pointers
        slow = head
        fast = head

        while(fast != None and fast.next != None and fast.next.next != None):
            slow = slow.next
            fast = fast.next.next
            if (slow.val == fast.val):
                return True
        return False