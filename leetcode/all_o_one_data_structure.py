class CountNode(object):
    def __init__(self, count, keys=None):
        self.count = count
        # keys are stored in a `set`, to make sure adding and removing to
        # be O(1).
        self.keys = set() if keys is None else keys
        self.prev = None
        self.next = None

    def __repr__(self):
        return "<Count: {}, Keys: {}> -> {}".format(
            self.count, self.keys,
            'None' if self.next is None else self.next)


class AllOne(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        # key - count pairs.
        self.key_count = {}

        # Double-linked list of count nodes with increase order.
        # Then the min key is the keys inside self.count_head.next, and the max
        # key is the keys inside self.count_tail.prev.
        self.count_head = CountNode(-2**32)
        self.count_tail = CountNode(2**31)
        self.count_head.next = self.count_tail
        self.count_tail.prev = self.count_head

    def _add_count_node(self, new_node, referent, add_before=False):
        if add_before:
            # Add the new_node before the referent.
            new_node.prev = referent.prev
            referent.prev.next = new_node
            referent.prev = new_node
            new_node.next = referent
        else:
            new_node.next = referent.next
            referent.next.prev = new_node
            referent.next = new_node
            new_node.prev = referent

    def _remove_count_node(self, current_node):
        prev_node = current_node.prev
        next_node = current_node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _update_count(self, key, new_count_num, referent, add_before):
        if referent.count == new_count_num:
            referent.keys.add(key)
            self.key_count[key] = referent
        else:
            new_node = CountNode(new_count_num, set([key]))
            self._add_count_node(new_node, referent, add_before)
            self.key_count[key] = new_node

    def inc(self, key):
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        :type key: str
        :rtype: void
        """
        print('Increasing {} ...'.format(key))
        if key not in self.key_count:
            self._update_count(key, 1, self.count_head.next, True)
        else:
            old_count = self.key_count[key]
            old_count.keys.remove(key)
            if not old_count.keys:
                self._remove_count_node(old_count)
            self._update_count(key, old_count.count + 1, old_count.next, True)


    def dec(self, key):
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        :type key: str
        :rtype: void
        """
        print('Decreasing {} ...'.format(key))
        if key not in self.key_count:
            return
        else:
            old_count = self.key_count[key]
            old_count.keys.remove(key)
            if not old_count.keys:
                self._remove_count_node(old_count)
            new_count_num = old_count.count - 1
            if new_count_num == 0:
                del self.key_count[key]
            else:
                self._update_count(key, new_count_num, old_count.prev, False)

    def getMaxKey(self):
        """
        Returns one of the keys with maximal value.
        :rtype: str
        """
        return ("" if self.count_tail.prev is self.count_head
                else list(self.count_tail.prev.keys)[0])

    def getMinKey(self):
        """
        Returns one of the keys with Minimal value.
        :rtype: str
        """
        return ("" if self.count_head.next is self.count_tail
                else list(self.count_head.next.keys)[0])


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
if __name__ == '__main__':
    
    a = AllOne()
    a.inc('A')
    a.inc('A')
    a.inc('B')
    a.inc('B')
    a.inc('B')
    a.inc('C')
    print('Current Count list: {}.'.format(a.count_head))
    print('Max Key: {}'.format(a.getMaxKey()))
    print('Min Key: {}'.format(a.getMinKey()))

    a.inc('C')
    print('Current Count list: {}.'.format(a.count_head))
    print('Max Key: {}'.format(a.getMaxKey()))
    print('Min Key: {}'.format(a.getMinKey()))

    a.dec('B')
    print('Current Count list: {}.'.format(a.count_head))
    print('Max Key: {}'.format(a.getMaxKey()))
    print('Min Key: {}'.format(a.getMinKey()))

    a.dec('B')
    a.dec('B')

    a.dec('A')

    a.dec('C')
    a.dec('C')
    print('Current Count list: {}.'.format(a.count_head))

    a.dec('A')
    a.dec('B')
    a.dec('C')
    print('Current Count list: {}.'.format(a.count_head))

    b = AllOne()
    b.inc('hello')
    print('Current Count list: {}.'.format(a.count_head))
    b.inc('hello')
    print('Max Key: {}'.format(b.getMaxKey()))
    print('Min Key: {}'.format(b.getMinKey()))
    b.inc('leet')
    print('Max Key: {}'.format(b.getMaxKey()))
    print('Min Key: {}'.format(b.getMinKey()))
