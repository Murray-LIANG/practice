"""
https://leetcode.com/problems/flatten-nested-list-iterator

Take [[1, 2], 2, [1, 2]] as example. Use stack to store the current progress of
iterating list/integer. The lower item in stack is the outer list, and the
upper items in stack are the nested list/int of outer list.

In initial state, the stack is like:
([[1,2], 2, [1,2]], 0).
Using 0 to indicate we are handling the first item [1,2] in list
[[1,2], 2, [1,2]]. Because [1,2] is another list, we push it into the stack:

([1,2], 0).
([[1,2], 2, [1,2]], 1).

Because the 0-th item of [1,2] is an int, we return true from has_next() and
change the index from 0 to 1, and return 1 from next(),

"""


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):
    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.stack = [(nestedList, 0)]

    def next(self):
        """
        :rtype: int
        """
        self.hasNext()
        nested, index = self.stack[-1]
        self.stack[-1][1] += 1
        return nested[index].getInteger()

    def hasNext(self):
        """
        :rtype: bool
        """
        s = self.stack
        while s:
            nested, index = s[-1]
            if index == len(nested):
                s.pop()
            else:
                tmp = nested[index]
                if tmp.isInteger():
                    return True
                s[-1][1] += 1
                s.append((tmp, 0))
        return False


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
