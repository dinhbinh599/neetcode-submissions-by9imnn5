# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        head = res

        if not list1 and not list2:
            return None

        while list1 or list2:
            if list1 and list2:
                if list1.val < list2.val:
                    res.val = list1.val
                    list1 = list1.next
                else:
                    res.val = list2.val
                    list2 = list2.next
            elif list1:
                res.val = list1.val
                list1 = list1.next
            else:
                res.val = list2.val
                list2 = list2.next

            if list1 or list2:
                res.next = ListNode()
                res = res.next

        return head