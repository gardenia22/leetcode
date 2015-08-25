# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} val
    # @return {ListNode}
    def removeElements(self, head, val):
        pre = None
        p = head
        while p:
            if p.val==val:
                if pre:
                    pre.next = p.next
                else:
                    head = p.next
            else:
                pre = p
            p = p.next    
        return head

a = Solution()
nodes = map(ListNode,[2,1,2,2,3,1,2])
for i in range(len(nodes)-1):
    nodes[i].next = nodes[i+1]
head = nodes[0]

head = a.removeElements(head,2)
while head:
    print head.val,
    head = head.next