# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        return self.addTwoNumbersRecursive(l1, l2, 0)

    def addTwoNumbersRecursive(self, l1: ListNode, l2: ListNode, c):
        val = l1.val + l2.val + c
        c = val // 10
        ret = ListNode(val % 10)

        if l1.next != None or l2.next != None:
            if not l1.next:
                l1.next = ListNode(0)
            if not l2.next:
                l2.next = ListNode(0)
            ret.next = self.addTwoNumbersRecursive(l1.next, l2.next, c)
        elif c:
            ret.next = ListNode(c)
        return ret
