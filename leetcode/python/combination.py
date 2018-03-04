
def comb(nums, k):
    if k == 0:
        return [[]]

    result = []

    for i, n in enumerate(nums):
        for suffix in comb(nums[i+1:], k-1):
            result.append([n] + suffix)

    return result

print(comb(range(1, 6), 3))

def comb2(nums, k):

    if k == 0 or not nums:
        return [[]]

    result = []
    suffixs = comb2(nums[1:], k-1)
    for s in suffixs:
        result.append([nums[0]] + s)

    if len(nums) > k:
        suffixs = comb2(nums[1:], k)
        result += suffixs

    return result

#print(filter(lambda x: len(x) == 3, comb2(range(1, 6), 3)))
print(comb2(range(1, 6), 3))
