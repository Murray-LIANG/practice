# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        all_val = []
        current = self
        while current is not None:
            all_val.append(str(current.val))
            current = current.next
        return ' -> '.join(all_val)

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        carry = 0
        dummy_head = current = ListNode(0)
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry, val = divmod(v1 + v2 + carry, 10)
            current.next = ListNode(val)
            current = current.next
        return dummy_head.next


if __name__ == '__main__':
    n3 = ListNode(3)
    n4 = ListNode(4)
    n4.next = n3
    l1 = ListNode(2)
    l1.next = n4

    n4 = ListNode(4)
    n6 = ListNode(6)
    n6.next = n4
    l2 = ListNode(5)
    l2.next = n6

    print('l1:      {}'.format(l1))
    print('l2:      {}'.format(l2))

    print('l1 + l2: {}'.format(Solution().addTwoNumbers(l1, l2)))


