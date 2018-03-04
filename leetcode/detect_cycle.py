# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return str(self.val)

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or head.next is None:
            return None

        slow = head
        fast = head

        while fast is not None:
            slow = slow.next
            if fast.next is None:
                return None
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None

        fast = head
        while fast != slow:
            fast = fast.next
            slow = slow.next

        return fast


if __name__ == '__main__':
    datas = [
        ([0, 1, 2, 3, 4], [1, 2, 3, 4, 2], 2),
        ([0, 1, 2, 3, 4], [1, 2, 3, 4, 1], 1),
        ([0, 1, 2, 3, 4], [1, 2, 3, 4, None], None),
        ([0, 1, 2, 3, 4], [1, 2, 3, 4, 4], 4),
        ([], [], None),
        ([0], [None], None),
    ]

    for nodes, links, expected in datas:
        mapping = {None: None}
        for node in nodes:
            mapping[node] = ListNode(node)

        for i in range(len(links)):
            mapping[i].next = mapping[links[i]]

        head = mapping[0] if 0 in mapping else None

        result = Solution().detectCycle(head)
        print('head: {}. Result: {}. Expected: {}'.format(
            links, result, expected == (result.val if result is not None
                                        else result)))
