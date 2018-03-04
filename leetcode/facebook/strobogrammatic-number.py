"""
A strobogrammatic number is a number that looks the same when rotated 180
degrees (looked at upside down).

Write a function to determine if a number is strobogrammatic. The number is
represented as a string.

For example, the numbers "69", "88", and "818" are all strobogrammatic.
"""

def is_equal(num1, num2):
    return (num1, num2) in (('0', '0'), ('1', '1'), ('8', '8'), ('6', '9'),
                            ('9', '6'))


def is_storbogrammatic(number):
    left, right = 0, len(number) - 1

    while left < right:
        if not is_equal(number[left], number[right]):
            return False
        left, right = left + 1, right - 1

    return True

print(is_storbogrammatic('88'))
print(is_storbogrammatic('68089'))
