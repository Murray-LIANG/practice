# https://leetcode.com/problems/lru-cache

from collections import deque


class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.key_list = deque([])
        self.obj_dict = {}


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.obj_dict:
            self.key_list.remove(key)
            self.key_list.append(key)
            return self.obj_dict[key]
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.get(key) == -1:
            if len(self.key_list) == self.capacity:
                evict_key = self.key_list.popleft()
                del self.obj_dict[evict_key]
            self.key_list.append(key)
        self.obj_dict[key] = value

# Your LRUCache object will be instantiated and called as such:
cache = LRUCache(2)
v_1 = cache.get(1)
print(v_1)
cache.put(1, 1)
v_1 = cache.get(1)
print(v_1)
cache.put(2, 2)
v_2 = cache.get(2)
print(v_2)
cache.put(3, 3)
v_3 = cache.get(3)
print(v_3)
v_1 = cache.get(1)
print(v_1)
v_2 = cache.get(2)
print(v_2)
