# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        carry = 0
        curr1 = l1
        curr2 = l2
        while (curr1 or curr2 or carry):
            v1 = curr1.val if curr1 else 0
            v2 = curr2.val if curr2 else 0

            nodeSum = v1 + v2 + carry
            nodedigit = nodeSum % 10
            carry = nodeSum // 10

            curr.next = ListNode(nodedigit)
            curr = curr.next

            curr1 = curr1.next if curr1 else 0
            curr2 = curr2.next if curr2 else 0
        
        return dummy.next