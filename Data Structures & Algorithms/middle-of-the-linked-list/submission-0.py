# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slowCurr = head
        fastCurr = head

        while fastCurr and fastCurr.next:
            slowCurr = slowCurr.next
            fastCurr = fastCurr.next.next

        return slowCurr