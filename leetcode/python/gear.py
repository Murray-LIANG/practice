def gear(nums):
    x = nums[-1] - nums[0] + 2 * sum(nums[1::2]) - 2 * sum(nums[2::2])

    if len(nums) % 2 == 0:
        x -= 2 * nums[-1]

    return ([-1, -1] if x <= 0
            else [2 * x, 3] if len(nums) % 2 == 0 else [2 * x, 1])


print(gear([4, 30]))
print(gear([4, 30, 50]))
print(gear([2, 30, 50, 64]))
print(gear([4, 17, 50]))
