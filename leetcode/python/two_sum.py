def two_sum_0(nums, target):
    # O(N^2)
    for i in range(0, len(nums)):
        rest = target - nums[i]
        for j in range(i + 1, len(nums)):
            if rest == nums[j]:
                return [i, j]
    return [-1, -1]

def two_sum_1(nums, target):
    # O(N)
    d = {} # num in nums as the key, index as the value
    for i in range(0, len(nums)):
        rest = target - nums[i]
        if rest not in d: #O(1)
            d[nums[i]] = i
        else:
            return [d[rest], i]
    return [-1, -1]

if __name__ == '__main__':
    test_data = [
        ([2, 7, 11, 15], 9),
        ([2, 7, 11, 15], 13),
        ([2, 7, 11, 15], 4),
        ([2, 7, 11, 15], 7),
        ([2, 7, 11, 15], 6),
        ([2], 6),
    ]

    for nums, target in test_data:
        print('two_sum_0 for nums: {}, target: {}'.format(nums, target))
        print('Result: {}'.format(two_sum_0(nums, target)))

        print('two_sum_1 for nums: {}, target: {}'.format(nums, target))
        print('Result: {}'.format(two_sum_1(nums, target)))
