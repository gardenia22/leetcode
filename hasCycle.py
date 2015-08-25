# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        if head and head.next and head.next:
            p1 = head.next
            p2 = head.next.next
            while p2 and p1!=p2:
                p1 = p1.next
                if p2.next:
                    p2 = p2.next.next
                else:
                    return False
            return p1==p2
        else:
            return False