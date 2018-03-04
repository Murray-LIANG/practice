# https://leetcode.com/problems/palindrome-linked-list

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False

        one_step = head
        two_step = head

        while two_step.next and two_step.next.next:
            one_step = one_step.next
            two_step = two_step.next.next

        second_half = self._reverse_link(one_step.next)

        while second_half:
            if head.val != second_half.val:
                return False
            head = head.next
            second_half = second_half.next

        return True

    @staticmethod
    def _reverse_link(head):
        pre = None
        while head:
            next = head.next
            head.next = pre
            pre = head
            head = next

        return pre

n1 = ListNode('1')
n2 = ListNode('2')
n3 = ListNode('3')
n4 = ListNode('2')
n5 = ListNode('1')
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

print(Solution().isPalindrome(n1))
