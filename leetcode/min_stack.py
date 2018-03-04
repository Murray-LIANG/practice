class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self._min = [2**32]
        self._vals = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self._min.append(min(self._min[-1], x))
        self._vals.append(x)

    def pop(self):
        """
        :rtype: void
        """
        self._min.pop()
        self._vals.pop()

    def top(self):
        """
        :rtype: int
        """
        return self._vals[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self._min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

if __name__ == '__main__':
    s = MinStack()
    s.push(-2)
    s.push(0)
    s.push(-3)
    print(s.getMin())
    s.pop()
    print(s.top())
    print(s.getMin())

