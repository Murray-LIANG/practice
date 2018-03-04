# https://leetcode.com/problems/design-phone-directory/description/

class PhoneDirectory(object):
    def __init__(self, maxNumbers):
        """
        Initialize your data structure here
        @param maxNumbers - The maximum numbers that can be stored in the phone directory.
        :type maxNumbers: int
        """
        self.availables = set(range(maxNumbers))

    def get(self):
        """
        Provide a number which is not assigned to anyone.
        @return - Return an available number. Return -1 if none is available.
        :rtype: int
        """
        return self.availables.pop() if self.availables else -1

    def check(self, number):
        """
        Check if a number is available or not.
        :type number: int
        :rtype: bool
        """
        return number in self.availables

    def release(self, number):
        """
        Recycle or release a number.
        :type number: int
        :rtype: void
        """
        self.availables.add(number)



        # Your PhoneDirectory object will be instantiated and called as such:
        # obj = PhoneDirectory(maxNumbers)
        # param_1 = obj.get()
        # param_2 = obj.check(number)
        # obj.release(number)
