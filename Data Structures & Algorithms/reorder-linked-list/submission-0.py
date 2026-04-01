# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    #write a function that reverses a list
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while (curr != None):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

    def reorderList(self, head: Optional[ListNode]) -> None:
        curr = head
        while (curr.next != None):
            temp = self.reverseList(curr.next)
            curr.next = temp
            curr = curr.next