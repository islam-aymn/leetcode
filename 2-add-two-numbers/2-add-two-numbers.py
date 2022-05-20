# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s = l1.val + l2.val

        r = s // 10
        s = s % 10

        result = cn = ListNode(s)

        while l1.next is not None or l2.next is not None or r:
            try:
                n1 = l1.next.val
            except AttributeError:
                n1 = 0

            try:
                n2 = l2.next.val
            except AttributeError:
                n2 = 0

            s = n1 + n2 + r

            r = s // 10
            s = s % 10

            cn.next = ListNode(s)

            if l1.next is not None:
                l1 = l1.next

            if l2.next is not None:
                l2 = l2.next

            cn = cn.next

        return result