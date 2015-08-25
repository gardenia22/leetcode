# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def swapPairs(self, head):
        p = head
        while p and p.next:
            temp = p.next.val
            p.next.val = p.val
            p.val = temp
            p = p.next.next
        return head
        