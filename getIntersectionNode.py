# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        pA, pB = headA, headB
        sizeA, sizeB = 0, 0
        while pA:
            sizeA += 1
            pA = pA.next
        while pB:
            sizeB += 1
            pB = pB.next
        while sizeA > sizeB:
            sizeA -= 1
            headA = headA.next
        while sizeB > sizeA:
            sizeB -= 1
            headB = headB.next
        while headA != headB:
            headA = headA.next
            headB = headB.next
        return headA