"""
A strobogrammatic number is a number that looks the same when rotated 180
degrees (looked at upside down).

Find all strobogrammatic numbers that are of length = n.

For example, Given n = 2, return ["11","69","88","96"].
"""


def fill(nums, left, right, res):
    if left > right:
        res.append(''.join(nums))
        return

    pairs = [('1', '1'), ('8', '8')]
    if left == right == 0 or left != 0:
        pairs.append(('0', '0'))
    if left != right:
        pairs += [('6', '9'), ('9', '6')]
    for pair in pairs:
        nums[left], nums[right] = pair[0], pair[1]
        fill(nums, left+1, right-1, res)

def all_storbogrammatic(n):
    if n == 0:
        return []

    nums = [''] * n
    res = []
    fill(nums, 0, n-1, res)
    return res

print(all_storbogrammatic(2))
print(all_storbogrammatic(3))
