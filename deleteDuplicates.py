# Definition for singly-linked list.
class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def deleteDuplicates1(self, head):
        zero = ListNode(0)
        zero.next = head
        p = zero
        while p and p.next:
            q = p.next
            while q.next and q.val == q.next.val:
                q = q.next
            if p.next is not q:
                p.next = q.next
            else:
                p = p.next
        return zero.next

    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = head
        flag = False
        while p:
            # delete duplicate nodes, other than the first dupicate node
            if p.next and p.next.val == p.val:
                p.next = p.next.next
                flag = True
            else:
                if flag:
                    # delete the fisrt duplicate node
                    if p.next:
                        # if the first deplicate node is not the tail
                        p.val = p.next.val
                        p.next = p.next.next
                    else:
                        # if the first deplicate node is the tail
                        p = head
                        pre = None
                        while p.next:
                            pre = p
                            p = p.next
                        if pre:
                            # if the first duplicated node is not the head
                            pre.next = None
                        else:
                            # if the first duplicated node is the head
                            head = pre
                else:
                    p = p.next
                flag = False
        return head

a = Solution()
nodes = map(ListNode, [0, 1, 1, 5, 6, 7, 7])
for i in range(len(nodes)-1):
    nodes[i].next = nodes[i+1]
head = nodes[0]

head = a.deleteDuplicates1(head)
while head:
    print head.val
    head = head.next
