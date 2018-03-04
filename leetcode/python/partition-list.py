# https://leetcode.com/problems/partition-list

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """

        left_head = ListNode(0)
        left_head.next = head
        right_head = ListNode(0)

        p = left_head
        i = head
        q = right_head

        while i is not None:
            while i is not None and i.val < x:
                p = i
                i = i.next
            q.next = i
            q = i
            if i is not None:
                p.next = i.next
                i = i.next

        p.next = right_head.next
        return left_head.next

def print_list(head):
    i = head
    while i is not None:
        print(i.val)
        i = i.next

n1 = ListNode(1)
n2 = ListNode(4)
n3 = ListNode(3)
n4 = ListNode(2)
n5 = ListNode(5)
n6 = ListNode(2)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6

Solution().partition(n1, 3)
print_list(n1)

n7 = ListNode(1)

Solution().partition(n7, 0)
print_list(n7)
