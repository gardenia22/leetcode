# Definition for singly-linked list.
class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param {ListNode} head
    # @return {ListNode}

    def sortList(self, head):
        if not head:
            return head
        p = head
        l = 0
        while p:
            p = p.next
            l += 1
        self.mergeSort(head, l)
        return head

    def mergeSort(self, head, l):
        if l == 1:
            return 0
        mid = l/2
        p = head
        for i in range(mid):
            p = p.next
        self.mergeSort(head, mid)
        self.mergeSort(p, l-mid)
        self.merge(head, mid, l)

    def merge(self, head, mid, l):
        p1 = p2 = head
        for i in range(mid):
            p2 = p2.next
        n1 = mid
        n2 = l-mid
        while n1:
            if n2 and p1.val > p2.val:
                # exchange value of p1 and p2
                temp = p1.val
                p1.val = p2.val
                p2.val = temp
                # insert p2 into the position between p1 and p1.next
                temp1 = p1.next
                p1.next = p2
                temp2 = p2.next
                p2.next = temp1
                # move p2 to p2.next, p1 remain same
                p2 = temp2
                p1 = p1.next
                n2 -= 1
            else:
                last = p1
                p1 = p1.next
                n1 -= 1
        last.next = p2

a = Solution()
nodes = map(ListNode, [2, 1, 4, 6, 7])
for i in range(len(nodes)-1):
    nodes[i].next = nodes[i+1]
head = nodes[0]

a.sortList(head)
while head:
    print head.val,
    head = head.next
